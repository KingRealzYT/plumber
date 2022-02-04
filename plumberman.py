from cmu_graphics import *

# Variables
app.background = 'Black'
app.startScreen = True
app.infoScreen = False
app.levelScreen = False
app.controlScreen = False
app.backButtonEnabled = False
app.mightyMeadows = False
app.menacingMountains = False
app.monstrousMoat = False
app.playButton = False
app.playerControlMovement = False
app.pauseControlScreenActive = False
app.playerMovement = False
app.pauseScreenActive = False
app.immortalPlayer = False
app.endGame = False
app.confirmExit = False

# Level 1 (MightyMeadows) Variables
app.mightyMeadowsScreen1 = False

# Player
player1 = Rect(0, 260, 20, 20, fill='red', visible=False)

# Level 1 Things
level1LGroup = Group()

level1Ground1 = Rect(0, 280, 400, 120, fill='green', visible=False)
level1Tree1 = Rect(160, 160, 40, 120, fill='brown', visible=False)
level1TreeLeaf11 = Rect(120, 120, 120, 40, fill='green', visible=False)
level1TreeLeaf12 = Rect(160, 80, 40, 40, fill='green', visible=False)

level1LGroup.add(level1Ground1)
level1LGroup.add(level1Tree1)
level1LGroup.add(level1TreeLeaf11)
level1LGroup.add(level1TreeLeaf12)

level1LGroup.visible = False

# Start screen
startGroup = Group()

gameName = Label('Plumber Man', 200, 40, fill='white', size=25)
gameInfo = Label('Info!', 80, 160, fill='white', size=25)
gameLevels = Label('Levels!', 320, 160, fill='white', size=25)
gameControls = Label('Controls!', 200, 280, fill='white', size=25)
gameStart = Label('Start!', 200, 200, fill='white', size=25)
instructionStartLabel = Label('Use your mouse to go over the text and press one of them', 200, 360, size=15, fill='white')

startGroup.add(gameName)
startGroup.add(gameInfo)
startGroup.add(gameLevels)
startGroup.add(gameControls)
startGroup.add(gameStart)
startGroup.add(instructionStartLabel)

# Exit Game Button
exitGameButtonLabel = Label('Exit!', 375, 20, fill='white', size=25)
exitGameButtonBackground = Rect(345, 0, 60, 40, fill='white', opacity=25, visible=False)

# Exit Confirmation
exitConfirmGroup = Group()

exitConfirmation1 = Rect(170, 90, 60, 70, fill=None, border='white', borderWidth=2, visible=False)
exitConfirmation2 = Label('Yes', 200, 110, fill='white', size=25, visible=False)
exitConfirmation3 = Label('No', 200, 140, fill='white', size=25, visible=False)
exitConfirmation4 = Rect(170, 90, 60, 36, fill='white', visible=False, opacity=25)
exitConfirmation5 = Rect(170, 126, 60, 36, fill='white', visible=False, opacity=25)

exitConfirmGroup.add(exitConfirmation1)
exitConfirmGroup.add(exitConfirmation2)
exitConfirmGroup.add(exitConfirmation3)
exitConfirmGroup.add(exitConfirmation4)
exitConfirmGroup.add(exitConfirmation5)

exitConfirmGroup.visible = False

# Hitboxes
gameNameHitbox = Rect(120, 20, 160, 40, fill='white', opacity=25, visible=False)
gameInfoHitbox = Rect(40, 140, 80, 40, fill='white', opacity=25, visible=False)
gameLevelHitbox = Rect(270, 140, 100, 40, fill='white', opacity=25, visible=False)
gameControlHitbox = Rect(140, 265, 120, 30, fill='white', opacity=25, visible=False)
gameStartHitbox = Rect(160, 180, 80, 40, fill='white', opacity=25, visible=False)

# Info Labels
infoLabelGroup = Group()

LabelInfo1 = Label('You are a plumber that is running across', 200, 200, size=15, fill='white', visible=False)
LabelInfo2 = Label('a map to get to the finish line', 200, 250, size=15, fill='white', visible=False)
LabelInfo3 = Label('to save the world!', 200, 300, size=15, fill='white', visible=False)

infoLabelGroup.add(LabelInfo1)
infoLabelGroup.add(LabelInfo2)
infoLabelGroup.add(LabelInfo3)

infoLabelGroup.visible = False

# Level Labels
levelChooserLabel1 = Label('1', 40, 80, fill='white', size=25, visible=False)
infoLabelLevel = Label('Use your mouse and left click a level!', 200, 280, fill='white', size=20, visible=False)
level1Name = Label('Mighty Meadows', 60, 120, fill='white', size=15, visible=False)

# Level Hitboxes
levelChooserLabel1Hitbox = Rect(25, 65, 30, 30, fill='white', opacity=25, visible=False)

# Level Borders
levelChooserLabel1Border = Rect(25, 65, 30, 30, fill=None, border='white', borderWidth=3, visible=False)

# Control Labels
leftControlLabel = Label('A = Left', 50, 105, fill='white', size=25, visible=False)
rightControlLabel = Label('D = Right', 60, 80, fill='white', size=25, visible=False)
pauseControlLabel = Label('P = Pause (In Level Only)', 150, 130, fill='white', size=25, visible=False)
unpauseControlLabel = Label('U = Unpause (In Level Only)', 165, 155, fill='white', size=25, visible=False)
cutControlLabel = Label('C = Phase through trees (Hold)', 180, 180, fill='white', size=25, visible=False)

# Control Test
controlGroup = Group()

controlTestGround = Rect(240, 320, 160, 80, fill='white', visible=False)
controlTestPlayer = Rect(320, 300, 20, 20, fill='red', visible=False)
tryItNowLabel = Label('Try The Keys Now!', 200, 220, fill='white', size=25, visible=False)
controlPMenu1 = Rect(35, 280, 90, 90, fill='white', visible=False)
controlPMenu2 = Label('Paused!', 80, 300, size=15, fill='black', visible=False)
controlPMenu3 = Label('Home', 80, 340, fill='black', size=15, visible=False)
controlPMenu4 = Rect(40, 320, 80, 40, fill=None, border='black', borderWidth=3, visible=False)

controlGroup.add(controlTestGround)
controlGroup.add(controlTestPlayer)
controlGroup.add(tryItNowLabel)
controlGroup.add(controlPMenu1)
controlGroup.add(controlPMenu2)
controlGroup.add(controlPMenu3)
controlGroup.add(controlPMenu4)
controlGroup.add(leftControlLabel)
controlGroup.add(rightControlLabel)
controlGroup.add(pauseControlLabel)
controlGroup.add(unpauseControlLabel)
controlGroup.add(cutControlLabel)

controlGroup.visible = False

# Back Variable
backLabel = Label('Back!', 40, 20, fill='white', size=25, visible=False)
backLabelHitbox = Rect(0, 0, 80, 40, fill='white', opacity=25, visible=False)

# Endgame Things
endGameLabels = Group()

gameFinishLabel = Label('Congrats! You Won!', 200, 200, size=25, fill='white', visible=False)
r2restartLabel = Label('Press R to Restart!', 200, 240, size=25, fill='white', visible=False)

endGameLabels.add(gameFinishLabel)
endGameLabels.add(r2restartLabel)
endGameLabels.visible = False

# Pause Menu
pauseMenuGroup = Group()

pauseMenu1 = Rect(140, 75, 120, 150, fill='black', border='white', borderWidth=3, visible=False)
pauseMenu2 = Label('Paused!', 200, 90, size=25, fill='white', visible=False)
pauseMenu3 = Label('Home!', 200, 150, size=20, fill='white', visible=False)
pauseMenu4 = Rect(160, 130, 80, 40, fill=None, border='white', borderWidth=3, visible=False)
pauseMenu5 = Label('U to Unpause', 200, 200, size=15, fill='white', visible=False)

pauseMenuGroup.add(pauseMenu1)
pauseMenuGroup.add(pauseMenu2)
pauseMenuGroup.add(pauseMenu3)
pauseMenuGroup.add(pauseMenu4)
pauseMenuGroup.add(pauseMenu5)

pauseMenuGroup.visible = False


# function that runs every second

def onStep():
    # Tree Hitbox Level 1
    if app.mightyMeadows:
        if not app.immortalPlayer:
            if level1Tree1.hitsShape(player1):
                app.playerControlMovement = False
                player1.centerX = 25
        if player1.centerX >= 400:
            startGroup.visible = False
            app.startScreen = False
            app.backButtonEnabled = False
            backLabel.visible = False
            backLabelHitbox.visible = False
            infoLabelGroup.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            infoLabelLevel.visible = False
            app.levelScreen = False
            controlGroup.visible = False
            app.controlScreen = False
            app.playerControlMovement = False
            app.pauseControlScreenActive = False
            app.background = 'black'
            player1.visible = False
            level1LGroup.visible = False
            app.playerMovement = False
            pauseMenuGroup.visible = False
            app.mightyMeadows = False
            app.endGame = True
            if app.endGame:
                endGameLabels.visible = True


# onMouseMove function

def onMouseMove(x, y):
    # Startscreen Hitboxes
    if app.startScreen:
        if gameNameHitbox.contains(x, y):
            gameNameHitbox.visible = True
        else:
            gameNameHitbox.visible = False

        if gameInfoHitbox.contains(x, y):
            gameInfoHitbox.visible = True
        else:
            gameInfoHitbox.visible = False

        if gameLevelHitbox.contains(x, y):
            gameLevelHitbox.visible = True
        else:
            gameLevelHitbox.visible = False

        if gameControlHitbox.contains(x, y):
            gameControlHitbox.visible = True
        else:
            gameControlHitbox.visible = False

        if gameStartHitbox.contains(x, y):
            gameStartHitbox.visible = True
        else:
            gameStartHitbox.visible = False

        if exitGameButtonBackground.contains(x, y):
            exitGameButtonBackground.visible = True
        else:
            exitGameButtonBackground.visible = False
        if app.confirmExit:
            if exitConfirmation4.contains(x, y):
                exitConfirmation4.visible = True
            else:
                exitConfirmation4.visible = False
            if exitConfirmation5.contains(x, y):
                exitConfirmation5.visible = True
            else:
                exitConfirmation5.visible = False

    # Levelscreen Hitbox
    if app.levelScreen:
        if levelChooserLabel1Hitbox.contains(x, y):
            levelChooserLabel1Hitbox.visible = True
        else:
            levelChooserLabel1Hitbox.visible = False

    # Back Button Hitbox
    if app.backButtonEnabled:
        if backLabelHitbox.contains(x, y):
            backLabelHitbox.visible = True
        else:
            backLabelHitbox.visible = False


def onMousePress(x, y):
    # If statements to check if a button is pressed
    if app.backButtonEnabled:
        if backLabelHitbox.contains(x, y):
            startGroup.visible = True
            app.startScreen = True
            app.backButtonEnabled = False
            backLabel.visible = False
            backLabelHitbox.visible = False
            infoLabelGroup.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            infoLabelLevel.visible = False
            app.levelScreen = False
            controlGroup.visible = False
            app.controlScreen = False
            app.playerControlMovement = False
            app.pauseControlScreenActive = True
            app.mightyMeadows = False
            level1Name.visible = False
            exitGameButtonLabel.visible = True

    if app.startScreen:
        if exitGameButtonBackground.contains(x, y):
            app.confirmExit = True
            exitConfirmGroup.visible = True
        if app.confirmExit:
            if exitConfirmation4.contains(x, y):
                exit()
            elif exitConfirmation5.contains(x, y):
                exitConfirmGroup.visible = False
                app.confirmExit = False
        if gameNameHitbox.contains(x, y):
            pass

        elif gameInfoHitbox.contains(x, y):
            startGroup.visible = False
            gameNameHitbox.visible = False
            gameInfoHitbox.visible = False
            gameLevelHitbox.visible = False
            gameControlHitbox.visible = False
            gameStartHitbox.visible = False
            app.startScreen = False
            backLabel.visible = True
            app.backButtonEnabled = True
            app.infoScreen = True
            exitGameButtonLabel.visible = False
            if app.infoScreen:
                infoLabelGroup.visible = True
        elif gameLevelHitbox.contains(x, y):
            startGroup.visible = False
            gameNameHitbox.visible = False
            gameInfoHitbox.visible = False
            gameLevelHitbox.visible = False
            gameControlHitbox.visible = False
            gameStartHitbox.visible = False
            app.startScreen = False
            app.levelScreen = True
            levelChooserLabel1Border.visible = True
            app.backButtonEnabled = True
            backLabel.visible = True
            exitGameButtonLabel.visible = False
            if app.levelScreen:
                levelChooserLabel1.visible = True
                infoLabelLevel.visible = True
                level1Name.visible = True

        elif gameControlHitbox.contains(x, y):
            startGroup.visible = False
            gameNameHitbox.visible = False
            gameInfoHitbox.visible = False
            gameLevelHitbox.visible = False
            gameControlHitbox.visible = False
            gameStartHitbox.visible = False
            app.startScreen = False
            app.controlScreen = True
            app.backButtonEnabled = True
            backLabel.visible = True
            exitGameButtonLabel.visible = False
            if app.controlScreen:
                controlGroup.visible = True
                controlPMenu1.visible = False
                controlPMenu2.visible = False
                controlPMenu3.visible = False
                controlPMenu4.visible = False
                app.pauseControlScreenActive = False
                app.playerControlMovement = True
            else:
                controlGroup.visible = False
                app.pauseControlScreenActive = False
                app.playerControlMovement = False

        elif gameStartHitbox.contains(x, y):
            startGroup.visible = False
            gameNameHitbox.visible = False
            gameInfoHitbox.visible = False
            gameLevelHitbox.visible = False
            gameControlHitbox.visible = False
            gameStartHitbox.visible = False
            app.startScreen = False
            app.mightyMeadows = True
            exitGameButtonLabel.visible = False
            if app.mightyMeadows:
                app.background = 'skyBlue'
                player1.visible = True
                level1LGroup.visible = True
                app.playerMovement = True

    # Controls Pause Menu
    elif app.controlScreen:
        if controlPMenu4.contains(x, y):
            startGroup.visible = True
            app.startScreen = True
            app.backButtonEnabled = False
            backLabel.visible = False
            backLabelHitbox.visible = False
            infoLabelGroup.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            infoLabelLevel.visible = False
            app.levelScreen = False
            controlGroup.visible = False
            app.controlScreen = False
            app.playerControlMovement = False
            app.pauseControlScreenActive = False
            app.mightyMeadows = False
            level1LGroup.visible = False
            app.pauseScreenActive = False
            level1Name.visible = False
            exitGameButtonLabel.visible = True

    elif app.mightyMeadows:
        if app.pauseScreenActive:
            if pauseMenu4.contains(x, y):
                startGroup.visible = True
                app.startScreen = True
                app.backButtonEnabled = False
                backLabel.visible = False
                backLabelHitbox.visible = False
                infoLabelGroup.visible = False
                levelChooserLabel1.visible = False
                levelChooserLabel1Border.visible = False
                infoLabelLevel.visible = False
                app.levelScreen = False
                controlGroup.visible = False
                app.controlScreen = False
                app.playerControlMovement = False
                app.pauseControlScreenActive = False
                app.background = 'black'
                player1.visible = False
                app.playerMovement = False
                pauseMenuGroup.visible = False
                app.mightyMeadows = False
                level1LGroup.visible = False
                app.pauseScreenActive = False
                level1Name.visible = False
                exitGameButtonLabel.visible = True

    elif app.levelScreen:
        if levelChooserLabel1Hitbox.contains(x, y):
            startGroup.visible = False
            gameNameHitbox.visible = False
            gameInfoHitbox.visible = False
            gameLevelHitbox.visible = False
            gameControlHitbox.visible = False
            gameStartHitbox.visible = False
            app.startScreen = False
            app.mightyMeadows = True
            backLabel.visible = False
            backLabelHitbox.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            levelChooserLabel1Hitbox.visible = False
            infoLabelLevel.visible = False
            app.backButtonEnabled = False
            app.levelScreen = False
            level1Name.visible = False
            exitGameButtonLabel.visible = False
            if app.mightyMeadows:
                app.background = 'skyBlue'
                player1.visible = True
                level1LGroup.visible = True
                app.playerMovement = True


def onKeyHold(keys):
    # Player Movement in Controls Screen
    if app.controlScreen:
        if app.playerControlMovement:
            if 250 < controlTestPlayer.centerX < 390:
                if 'd' in keys:
                    controlTestPlayer.centerX += 5
                elif 'a' in keys:
                    controlTestPlayer.centerX -= 5
            else:
                controlTestPlayer.centerX = 320
    elif app.mightyMeadows:
        if app.playerMovement:
            if 10 <= player1.centerX <= 395:
                if 'd' in keys:
                    player1.centerX += 5
                    player1.toFront()
                elif 'a' in keys:
                    player1.centerX -= 5
                    player1.toFront()
            else:
                player1.centerX = 25
        if 'c' in keys:
            app.immortalPlayer = True


def onKeyRelease(key):
    if key == 'c':
        app.immortalPlayer = False


def onKeyPress(key):
    if app.controlScreen:
        if key == 'p':
            app.playerControlMovement = False
            controlPMenu1.visible = True
            controlPMenu2.visible = True
            controlPMenu3.visible = True
            controlPMenu4.visible = True
            app.pauseControlScreenActive = True

        elif key == 'P':
            app.playerControlMovement = False
            controlPMenu1.visible = True
            controlPMenu2.visible = True
            controlPMenu3.visible = True
            controlPMenu4.visible = True
            app.pauseControlScreenActive = True

        elif key == 'u':
            app.playerControlMovement = True
            controlPMenu1.visible = False
            controlPMenu2.visible = False
            controlPMenu3.visible = False
            controlPMenu4.visible = False
            app.pauseControlScreenActive = False

        elif key == 'U':
            app.playerControlMovement = True
            controlPMenu1.visible = False
            controlPMenu2.visible = False
            controlPMenu3.visible = False
            controlPMenu4.visible = False
            app.pauseControlScreenActive = False

    if app.mightyMeadows:
        if key == 'p':
            app.playerMovement = False
            pauseMenuGroup.visible = True
            app.pauseScreenActive = True

        elif key == 'P':
            app.playerMovement = False
            pauseMenuGroup.visible = True
            app.pauseScreenActive = True

        elif key == 'u':
            app.playerMovement = True
            pauseMenuGroup.visible = False
            app.pauseScreenActive = False

        elif key == 'U':
            app.playerMovement = True
            pauseMenuGroup.visible = False
            app.pauseScreenActive = False

    if app.endGame:
        if key == 'r':
            startGroup.visible = True
            app.startScreen = True
            app.backButtonEnabled = False
            backLabel.visible = False
            backLabelHitbox.visible = False
            infoLabelGroup.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            infoLabelLevel.visible = False
            app.levelScreen = False
            controlGroup.visible = False
            app.controlScreen = False
            app.playerControlMovement = False
            app.pauseControlScreenActive = False
            app.background = 'black'
            player1.visible = False
            level1LGroup.visible = False
            app.playerMovement = False
            pauseMenuGroup.visible = False
            app.mightyMeadows = False
            endGameLabels.visible = False
            app.endGame = False
            player1.centerX = 0
            app.pauseScreenActive = False
            exitGameButtonLabel.visible = True
    elif key == 'R':
        startGroup.visible = True
        app.startScreen = True
        app.backButtonEnabled = False
        backLabel.visible = False
        backLabelHitbox.visible = False
        infoLabelGroup.visible = False
        levelChooserLabel1.visible = False
        levelChooserLabel1Border.visible = False
        infoLabelLevel.visible = False
        app.levelScreen = False
        controlGroup.visible = False
        app.controlScreen = False
        app.playerControlMovement = False
        app.pauseControlScreenActive = False
        app.background = 'black'
        player1.visible = False
        level1LGroup.visible = False
        app.playerMovement = False
        pauseMenuGroup.visible = False
        app.mightyMeadows = False
        endGameLabels.visible = False
        app.endGame = False
        player1.centerX = 0
        app.pauseScreenActive = False


cmu_graphics.run()
