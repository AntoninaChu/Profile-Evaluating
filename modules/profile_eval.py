from InstagramAPI import InstagramAPI
from linked_list import LinkedList
from array import Array
from get_comments_likes import get_comment, get_likes
import random

class Profile_Eval:
    '''This class presents a system that will look for a winner of
    Instagram Give Away.'''

    def __init__(self):
        '''This function creates an object of Profile_Eval class and sets
        all class variables.'''
        self._menu = ('\n[1] Set a place for searching a winner.\n'
                        '[2] Add a post to check comments.\n'
                        '[3] Add a post to check likes.\n'
                        '[4] Add a profile to check subscriptions\n'
                        '[5] Start searching.\n'
                        'Enter a number of action: ')
        self._look_in = LinkedList()
        self._check_likes = LinkedList()
        self._check_comments = LinkedList()
        self._check_subscriptions = LinkedList()
        self._result = None

    def _data_collecting(self):
        '''This function prints all options of actions, takes a choice and
        process it. This function works in recursion, until user will stop it.'''
        choice = input(self._menu)
        if choice == '1':
            self._set_look_in()
            self._data_collecting()
        elif choice == '2':
            self._add_check_comments(self._check_comments)
            self._data_collecting()
        elif choice == '3':
            self._add_check_likes(self._check_likes)
            self._data_collecting()
        elif choice == '4':
            self._add_check_subscriptions(self._check_subscriptions)
            self._data_collecting()
        elif choice == '5':
            while self._result == None:
                self.search_process()
                if self._result != -1:
                    self._check_requirements(self._check_likes)
                    self._check_requirements(self._check_comments)
                    self._check_requirements(self._check_subscriptions)
            self._return_results()
        else:
            print('wrong acction!')
            self._data_collecting()

    def _set_look_in(self):
        '''This function sets an Array of usernames, from which program need to
        choose a winner.'''
        if len(self._look_in) != 0:
            print('You already set this!')
            return -1
        data_type = input('Enter a number of data type you want to set(1. likes, 2. comments, 3. subscriptions): ')
        if data_type == '1':
            self._add_check_likes(self._look_in)
        elif data_type == '2':
            self._add_check_comments(self._look_in)
        elif data_type == '3':
            self._add_check_subscriptions(self._look_in)
        else:
            print('wrong acction!')

    def _add_check_subscriptions(self, ll_to_save):
        '''This function sets an linked list of arrays that hold usernames of
        subscribers. Winner must be in each Array of that lined list.'''
        login = input('Enter your username: ')
        password = input('Enter your password: ')
        try:
            API = InstagramAPI(login, password)
            API.login()
            res = API.getTotalSelfFollowers()
        except:
            print('Wrong data or password!')
            self._data_collecting()
        arr = Array(len(res))
        for num, follower in enumerate(res):
            arr[num] = follower['username']
        ll_to_save.add_data(arr)

    def _add_check_likes(self, ll_to_save):
        '''This function sets an linked list of arrays that hold usernames of
        likers. Winner must be in each Array of that lined list.'''
        login = input('Enter your username: ')
        password = input('Enter your password: ')
        image_url = input('Enter an url of your post: ')
        try:
            API = InstagramAPI(login, password)
            API.login()
            media_id = API.get_media_id(image_url)
            res = get_likes(login, password, media_id)
        except:
            print('Wrong data or password!')
            self._data_collecting()
        arr = Array(len(res))
        for num, username in enumerate(res):
            arr[num] = username
        ll_to_save.add_data(arr)

    def _add_check_comments(self, ll_to_save):
        '''This function sets an linked list of arrays that hold usernames of
        likers. Winner must be in each Array of that lined list.'''
        login = input('Enter your username: ')
        password = input('Enter your password: ')
        image_url = input('Enter an url of your post: ')
        try:
            API = InstagramAPI(login, password)
            API.login()
            media_id = API.get_media_id(image_url)
            res = get_comment(login, password, media_id)
        except:
            print('Wrong login or password!')
            self._data_collecting()
        arr = Array(len(res))
        for num, username in enumerate(res):
            arr[num] = username
        ll_to_save.add_data(arr)

    def search_process(self):
        '''This function randomly choose a user from _look_in Array.'''
        if self._look_in._head == None:
            print(' YOU DIDN`T SET PLACE TO LOOK IN YET!')
            self._result = -1
            return
        r_int = random.randint(0, len(self._look_in._head.data)-1)
        self._result = self._look_in._head.data[r_int]

    def _check_requirements(self, ll_to_search):
        '''This function takes a linked list and checks if self._result is in
        esch of arrays from that linked list.'''
        cur_node = ll_to_search._head
        found = False
        while  cur_node != None:
            for name in cur_node.data:
                if self._result == name:
                    found = True
                    break
            if found == False:
                self._result = None
                return False
            cur_node = cur_node.next
        return True

    def _return_results(self):
        '''This function prints a username of winner.'''
        print('Your winner is ', self._result)
