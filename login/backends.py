from django.conf import settings
from django.contrib.auth.models import User, check_password
from entradas.models import Empleado, DondeTrabaja
import ldap

class SettingsBackend:
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name, and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'sha1$4e987$afbcf42e21bd417fb71db8c66b321e9fc33051de'
    """
    def authenticate(self, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. Note that we can set password
                # to anything, because it won't be checked; the password
                # from settings.py will.
                user = User(username=username, password='get from settings.py')
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class LDAPBackend:
    """http://www.carthage.edu/webdev/?p=12


    """
    def authenticate(self, username=None, password=None):

        # Authenticate the base user so we can search
        try:
            l = ldap.open(settings.AUTH_LDAP_SERVER)
            l.protocol_version = ldap.VERSION3

            userldap="uid="+username+", "+ settings.AUTH_LDAP_BASE

            # Attempt to bind to the user's DN
            l.simple_bind_s(userldap,password)
            # The user existed and authenticated. Get the user
            # record or create one with no privileges.
            try:
                user = User.objects.get(username__exact=username)
            except:
                # Antes creabamos el usuario. Ahora tenemos la bd poblada
                # sino esta en ella no permitimos el acceso
                #return None
                # cambiar a esto:
                # mail, first_name, last_name
                scope = ldap.SCOPE_SUBTREE
                filter = "(&(objectclass=person) (uid=%s))" % username
                ret = ['dn', 'givenName','sn']

                ldap_result_id = l.search(settings.AUTH_LDAP_BASE, scope,filter,ret)
                result_set = []

                while 1:
                    result_type, result_data = l.result(ldap_result_id, 0)
                    if result_data == []:
                        break
                    else:
                        if result_type == ldap.RES_SEARCH_ENTRY:
                            result_set.append(result_data)

                dn = result_set.pop()

                if dn[0][1].has_key('mail'):
                    mail = dn[0][1]['mail'][0]
                else:
                    mail = username + '@juntadeandalucia.es'

                if dn[0][1]['givenName'][-1] != None:
                    givenname =dn[0][1]['givenName'][-1]
                else:
                    givenname = username

                if dn[0][1]['sn'][-1] != None:
                    sn=dn[0][1]['sn'][-1].strip()
                else:
                    sn =username

                user = User.objects.create_user(username,mail)
                user.first_name = givenname
                user.last_name = sn
                user.mail = mail
                user.is_active= True
                user.save()
                # almacenamos tb empleados Por defecto departamento desconocido (id = 50) TODO: poner inteligencia aqui por el momento no hace falta
                dondeT=DondeTrabaja(pk=50)
                empleado = Empleado (user=user,nombre=user.first_name+" "+user.last_name,trabajaen=dondeT,permisos='a')
                empleado.save()
            # Success.
            return user
           
        except ldap.INVALID_CREDENTIALS:
            # Name or password were bad. Fail.
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
