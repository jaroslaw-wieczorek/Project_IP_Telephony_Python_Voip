import os
import sys

lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)
lib_path2 = os.path.abspath(os.path.join(__file__, '..','..','..'))
sys.path.append(lib_path2)

from JaroEliCall.src.functionality.my_app import MyApp
from JaroEliCall.src.functionality.login_dialog import LoginDialog
from JaroEliCall.src.functionality.main_window_dialog import MainWindowDialog
from JaroEliCall.src.functionality.register_dialog import RegisterDialog
from JaroEliCall.src.functionality.interaction_dialog import InteractionDialog
from JaroEliCall.src.functionality.password_change_dialog import PasswordChangeDialog

from JaroEliCall.src.client import Client


def main():

    client = Client()
    myapp = MyApp(sys.argv)


    myapp.setupClient(client)


    loginWindow = LoginDialog(myapp.client)
    myapp.setupLoginWindow(loginWindow)

    registerWindow = RegisterDialog(myapp.client)
    myapp.setupRegisterWindow(registerWindow)

    mainAppWindow = MainWindowDialog(myapp.client)
    myapp.setupMainWindow(mainAppWindow)

    interactionWindow = InteractionDialog(myapp.client)
    myapp.setupInteractionWindow(interactionWindow)

    activationWindow = PasswordChangeDialog(myapp.client)
    myapp.setupActivationWindow(activationWindow)


    # Signal use to hide login dialog when logging passeds
    myapp.loginWindow.loggingSignal.connect(myapp.loggingSignalResponse)
    myapp.loginWindow.registerAccountSignal.connect(myapp.registerAccountSignalResponse)


    # Signal use to hide login dialog and show register dialog
    myapp.registerWindow.registrationSignal.connect(myapp.registerSignalResponse)
    myapp.registerWindow.alreadyAccountSignal.connect(myapp.alreadyAccountSignalResponse)
    myapp.client.registerMessage.connect(myapp.registerMessageResponse)

    myapp.mainWindow.closingSignal.connect(myapp.closingSignalResponse)
    #myapp.loginWindow.closingSignal.connect(myapp.closingSignalResponse)
    #myapp.registerWindow.closingSignal.connect(myapp.closingSignalResponse)

    myapp.client.getMessage.connect(myapp.loginWindow.loop.quit)
    myapp.client.getMessage.connect(myapp.mainWindow.loop.quit)


    # Making call to someone
    myapp.client.makeCallSignal.connect(myapp.interactionWindow.loop.quit)

    # Connect recive invite from someone to show interaction_dialog
    myapp.client.getCallSignal.connect(myapp.mainWindow.loop.quit)
    myapp.client.getCallSignal.connect(myapp.getCallSignalResponse)

    myapp.client.activateAccountMessage.connect(myapp.activationSignalResponse)

    myapp.client.changedPasswordMessage.connect(myapp.changedPasswordMessageResponse)

    myapp.client.endCallResponse.connect(myapp.endCallResponseResponse)

    # People receive info that they can show interface "Rozmowa z ...
    myapp.client.callSignal.connect(myapp.callSignalResponse)

    myapp.client.changedUsersStatusSignal.connect(myapp.changedUsersStatusResponse)

    myapp.interactionWindow.endCallSignal.connect(myapp.endCallResponse)
    # myapp.client.callSignal.connect(myapp.client.sendingVoice)

    # Reaction on clicked accept or reject button
    # myapp.interactionWindow.callAnswerSignal.connect(myapp.client.sendingVoice)

    myapp.showLoginWindow()

    sys.exit(myapp.exec_())



if __name__ == "__main__":
    main()
