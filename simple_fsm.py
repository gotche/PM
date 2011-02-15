class StatesMachine:
    fsm_boss = {
        'just_created' :  {'done': 'done', 'todo': 'in_future', 'delegate': 'delegated'},
        'done' : {'re-open': 'just_created'},
        'in_future' : {'done': 'done','delegate': 'delegated' },
        'delegated' : {'ask_info': 'delegated'},
        'rejected' : {'ask_info': 'delegated', 'close': 'closed'},
        'solved' : {'reject': 'delegated', 'close': 'closed'},
        'rejected' : {'ask_info': 'delegated', 'close': 'closed'},

    }
    fsm_worker = {

        'delegated' : {'done': 'done_delegated', 'reject': 'rejected', },
        'solved' : {'reject': 'delegated', 'close': 'closed'},

    }

    @classmethod
    def next_state(cls,state,inputm, owner=True):
   
        if owner:
            fsm = cls.fsm_boss
        else:
            fsm = cls.fsm_worker
 
        if state in fsm.keys():
            if inputm in fsm[state].keys():
                print fsm[state][inputm]
            else: print "No"
        else: print "No No" 

   
if __name__ == '__main__':
    s = StatesMachine()
    s.next_state('solved','close') 
    StatesMachine.next_state('solved','close')
