

def __init__(self)
    
    # self.subscribe('chatbot', self.callback_fnc)
    # self.pub = self.make_publisher('chatbot_ack')
    # self.text = None 
    self.action_server = XXXXXX


def callback_fnc(self, txt):
    self.text = txt

def main(self):

    #listen to what user say
    # self.pub('listen_now!!!')

    # # everything after this should run AFTER you receive what the person said
    # ######
    # while self.text != None:
    #     sleep(0.1)

    self.action_server.send_request('text')
    robot_move
    self.action_server.wait_for_result()
    # result = self.action_server


    print(f"the person say {self.text}")