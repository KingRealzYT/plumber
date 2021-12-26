from cmu_graphics import *

# Initial background
app.background = 'Black'
app.startScreen = True
app.infoScreen = False
app.levelScreen = False
app.controlScreen = False
app.backButtonEnabled = False
app.mistyMeadows = False
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

# Cursor
cursor1 = Line(195, 235, 190, 230, fill='white')
cursor2 = RegularPolygon(190, 230, 5, 3, fill='white', rotateAngle=-45)

# Player
player1 = Rect(0, 260, 20, 20, fill='red', visible=False)

# Level 1 Things
level1Ground1 = Rect(0, 280, 400, 120, fill='green', visible=False)
level1Tree1 = Rect(160, 160, 40, 120, fill='brown', visible=False)
level1TreeLeaf11 = Rect(120, 120, 120, 40, fill='green', visible=False)
level1TreeLeaf12 = Rect(160, 80, 40, 40, fill='green', visible=False)
level1TreeBorder = Rect(120, 120, 120, 160, fill=None, visible=False)

# Start screen
gameName = Label('Plumber Man', 200, 40, fill='white', size=25)
gameInfo = Label('Info!', 80, 160, fill='white', size=25)
gameLevels = Label('Levels!', 320, 160, fill='white', size=25)
gameControls = Label('Controls!', 200, 280, fill='white', size=25)
gameStart = Label('Start!', 200, 200, fill='white', size=25)
instructionStartLabel = Label('Use your mouse to go over the text and press one of them', 200, 360, size=15,
                              fill='white')

# Exit Game Button
exitGameButtonLabel = Label('Exit!', 375, 20, fill='white', size=25)
exitGameButtonBackground = Rect(345, 0, 60, 40, fill='white', opacity=25, visible=False)

# Exit Confirmation
exitConfirmation1 = Rect(170, 90, 60, 70, fill=None, border='white', borderWidth=2, visible=False)
exitConfirmation2 = Label('Yes', 200, 110, fill='white', size=25, visible=False)
exitConfirmation3 = Label('No', 200, 140, fill='white', size=25, visible=False)
exitConfirmation4 = Rect(170, 90, 60, 40, fill='white', visible=False, opacity=25)
exitConfirmation5 = Rect(170, 120, 60, 40, fill='white', visible=False, opacity=25)

# Hitboxes
gameNameHitbox = Rect(120, 20, 160, 40, fill='white', opacity=25, visible=False)
gameInfoHitbox = Rect(40, 140, 80, 40, fill='white', opacity=25, visible=False)
gameLevelHitbox = Rect(270, 140, 100, 40, fill='white', opacity=25, visible=False)
gameControlHitbox = Rect(140, 265, 120, 30, fill='white', opacity=25, visible=False)
gameStartHitbox = Rect(160, 180, 80, 40, fill='white', opacity=25, visible=False)

# Info Labels
LabelInfo1 = Label('This game is inspired by Mario, You are a plumber', 200, 200, size=15, fill='white', visible=False)
LabelInfo2 = Label('that is running across a map to get to the finish line', 200, 250, size=15, fill='white',
                   visible=False)
LabelInfo3 = Label('and save the world!', 95, 300, size=15, fill='white', visible=False)

# Level Labels
levelChooserLabel1 = Label('1', 40, 80, fill='white', size=25, visible=False)
infoLabelLevel = Label('Use your mouse and left click a level!', 200, 280, fill='white', size=20, visible=False)
level1Name = Label('Misty Meadows', 100, 120, fill='white', size=25, visible=False)

# Level Hitboxes
levelChooserLabel1Hitbox = Rect(25, 65, 30, 30, fill='white', opacity=25, visible=False)

# Level Borders
levelChooserLabel1Border = Rect(25, 65, 30, 30, fill=None, border='white', borderWidth=3, visible=False)

# Control Test
controlTestGround = Rect(240, 320, 160, 80, fill='white', visible=False)
controlTestPlayer = Rect(320, 300, 20, 20, fill='red', visible=False)
tryItNowLabel = Label('Try The Keys Now!', 200, 220, fill='white', size=25, visible=False)
controlPMenu1 = Rect(35, 280, 90, 90, fill='white', visible=False)
controlPMenu2 = Label('Paused!', 80, 300, size=15, fill='black', visible=False)
controlPMenu3 = Label('Home', 80, 340, fill='black', size=15, visible=False)
controlPMenu4 = Rect(40, 320, 80, 40, fill=None, border='black', borderWidth=3, visible=False)

# Control Labels
leftControlLabel = Label('A = Left', 50, 105, fill='white', size=25, visible=False)
rightControlLabel = Label('D = Right', 60, 80, fill='white', size=25, visible=False)
pauseControlLabel = Label('P = Pause (In Level Only)', 150, 130, fill='white', size=25, visible=False)
unpauseControlLabel = Label('U = Unpause (In Level Only)', 165, 155, fill='white', size=25, visible=False)
cutControlLabel = Label('C = Phase through trees (Hold)', 180, 180, fill='white', size=25, visible=False)
# Back Variable
backLabel = Label('Back!', 40, 20, fill='white', size=25, visible=False)
backLabelHitbox = Rect(0, 0, 80, 40, fill='white', opacity=25, visible=False)

# Endgame Things
gameFinishLabel = Label('Congrats! You Won!', 200, 200, size=25, fill='white', visible=False)
r2restartLabel = Label('Press R to Restart!', 200, 240, size=25, fill='white', visible=False)

# Pause Menu
pauseMenu1 = Rect(140, 75, 120, 150, fill='black', border='white', borderWidth=3, visible=False)
pauseMenu2 = Label('Paused!', 200, 90, size=25, fill='white', visible=False)
pauseMenu3 = Label('Home!', 200, 150, size=20, fill='white', visible=False)
pauseMenu4 = Rect(160, 130, 80, 40, fill=None, border='white', borderWidth=3, visible=False)
pauseMenu5 = Label('U to Unpause', 200, 200, size=15, fill='white', visible=False)


# function that runs every second

def onStep():
    # Startscreen Hitboxes
    if app.startScreen:
        if gameNameHitbox.containsShape(cursor1) or gameNameHitbox.containsShape(cursor2):
            gameNameHitbox.visible = True
        else:
            gameNameHitbox.visible = False

        if gameInfoHitbox.containsShape(cursor1) or gameInfoHitbox.containsShape(cursor2):
            gameInfoHitbox.visible = True
        else:
            gameInfoHitbox.visible = False

        if gameLevelHitbox.containsShape(cursor1) or gameLevelHitbox.containsShape(cursor2):
            gameLevelHitbox.visible = True
        else:
            gameLevelHitbox.visible = False

        if gameControlHitbox.containsShape(cursor1) or gameControlHitbox.containsShape(cursor2):
            gameControlHitbox.visible = True
        else:
            gameControlHitbox.visible = False

        if gameStartHitbox.containsShape(cursor1) or gameStartHitbox.containsShape(cursor2):
            gameStartHitbox.visible = True
        else:
            gameStartHitbox.visible = False

        if exitGameButtonBackground.containsShape(cursor1) or exitGameButtonBackground.containsShape(cursor2):
            exitGameButtonBackground.visible = True
        else:
            exitGameButtonBackground.visible = False
        if app.confirmExit:
            if exitConfirmation4.containsShape(cursor1) or exitConfirmation4.containsShape(cursor2):
                exitConfirmation4.visible = True
            else:
                exitConfirmation4.visible = False
            if exitConfirmation5.containsShape(cursor1) or exitConfirmation5.containsShape(cursor2):
                exitConfirmation5.visible = True
            else:
                exitConfirmation5.visible = False

    # Control Pause Menu Hitbox
    if app.controlScreen:
        if app.pauseControlScreenActive:
            if controlPMenu1.containsShape(cursor1) or controlPMenu1.containsShape(cursor2):
                cursor1.fill = 'black'
                cursor2.fill = 'black'
                cursor1.toFront()
                cursor2.toFront()
            else:
                cursor1.fill = 'white'
                cursor2.fill = 'white'
        else:
            cursor1.fill = 'white'
            cursor2.fill = 'white'

    # Tree Hitbox Level 1
    if app.mistyMeadows:
        if not app.immortalPlayer:
            if level1Tree1.hitsShape(player1):
                app.playerControlMovement = False
                player1.centerX = 25
        if player1.centerX >= 400:
            gameName.visible = False
            gameInfo.visible = False
            gameLevels.visible = False
            gameControls.visible = False
            gameStart.visible = False
            app.startScreen = False
            instructionStartLabel.visible = False
            app.backButtonEnabled = False
            backLabel.visible = False
            backLabelHitbox.visible = False
            LabelInfo1.visible = False
            LabelInfo2.visible = False
            LabelInfo3.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            infoLabelLevel.visible = False
            app.levelScreen = False
            rightControlLabel.visible = False
            leftControlLabel.visible = False
            pauseControlLabel.visible = False
            unpauseControlLabel.visible = False
            controlTestGround.visible = False
            controlTestPlayer.visible = False
            tryItNowLabel.visible = False
            app.controlScreen = False
            app.playerControlMovement = False
            controlPMenu1.visible = False
            controlPMenu2.visible = False
            controlPMenu3.visible = False
            controlPMenu4.visible = False
            app.pauseControlScreenActive = False
            cursor1.fill = 'white'
            cursor2.fill = 'white'
            cursor1.visible = True
            cursor2.visible = True
            app.background = 'black'
            player1.visible = False
            level1Ground1.visible = False
            app.playerMovement = False
            pauseMenu1.visible = False
            pauseMenu2.visible = False
            pauseMenu3.visible = False
            pauseMenu4.visible = False
            pauseMenu5.visible = False
            cutControlLabel.visible = False
            app.mistyMeadows = False
            level1Tree1.visible = False
            level1TreeLeaf11.visible = False
            level1TreeLeaf12.visible = False
            app.endGame = True
            if app.endGame:
                gameFinishLabel.visible = True
                r2restartLabel.visible = True

    # Levelscreen Hitbox
    if app.levelScreen:
        if levelChooserLabel1Hitbox.containsShape(cursor1) or levelChooserLabel1Hitbox.containsShape(cursor2):
            levelChooserLabel1Hitbox.visible = True
        else:
            levelChooserLabel1Hitbox.visible = False

    # Back Button Hitbox
    if app.backButtonEnabled:
        if backLabelHitbox.containsShape(cursor1) or backLabelHitbox.containsShape(cursor2):
            backLabelHitbox.visible = True
        else:
            backLabelHitbox.visible = False


# onMouseMove function

def onMouseMove(x, y):
    # Move the cursor
    cursor1.x1 = x
    cursor1.y1 = y
    cursor1.x2 = x - 5
    cursor1.y2 = y - 5
    cursor2.centerX = cursor1.x2
    cursor2.centerY = cursor1.y2


def onMousePress(x, y):
    # If statements to check if a button is pressed
    if app.backButtonEnabled:
        if backLabelHitbox.containsShape(cursor1) or backLabelHitbox.containsShape(cursor2):
            gameName.visible = True
            gameInfo.visible = True
            gameLevels.visible = True
            gameControls.visible = True
            gameStart.visible = True
            app.startScreen = True
            instructionStartLabel.visible = True
            app.backButtonEnabled = False
            backLabel.visible = False
            backLabelHitbox.visible = False
            LabelInfo1.visible = False
            LabelInfo2.visible = False
            LabelInfo3.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            infoLabelLevel.visible = False
            app.levelScreen = False
            rightControlLabel.visible = False
            leftControlLabel.visible = False
            pauseControlLabel.visible = False
            unpauseControlLabel.visible = False
            controlTestGround.visible = False
            controlTestPlayer.visible = False
            tryItNowLabel.visible = False
            app.controlScreen = False
            app.playerControlMovement = False
            controlPMenu1.visible = False
            controlPMenu2.visible = False
            controlPMenu3.visible = False
            controlPMenu4.visible = False
            app.pauseControlScreenActive = True
            cutControlLabel.visible = False
            app.mistyMeadows = False
            level1Name.visible = False
            exitGameButtonLabel.visible = True

    if app.startScreen:
        if exitGameButtonBackground.containsShape(cursor1) or exitGameButtonBackground.containsShape(cursor2):
            app.confirmExit = True
            exitConfirmation1.visible = True
            exitConfirmation2.visible = True
            exitConfirmation3.visible = True
            exitConfirmation4.visible = True
            exitConfirmation5.visible = True
        if app.confirmExit:
            if exitConfirmation4.containsShape(cursor1) or exitConfirmation4.containsShape(cursor2):
                exit()
            elif exitConfirmation5.containsShape(cursor1) or exitConfirmation5.containsShape(cursor2):
                exitConfirmation1.visible = False
                exitConfirmation2.visible = False
                exitConfirmation3.visible = False
                exitConfirmation4.visible = False
                exitConfirmation5.visible = False
                app.confirmExit = False
        if gameNameHitbox.containsShape(cursor1) or gameNameHitbox.containsShape(cursor2):
            pass

        elif gameInfoHitbox.containsShape(cursor1) or gameInfoHitbox.containsShape(cursor2):
            gameName.visible = False
            gameInfo.visible = False
            gameLevels.visible = False
            gameControls.visible = False
            gameStart.visible = False
            instructionStartLabel.visible = False
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
                LabelInfo1.visible = True
                LabelInfo2.visible = True
                LabelInfo3.visible = True
        elif gameLevelHitbox.containsShape(cursor1) or gameLevelHitbox.containsShape(cursor2):
            gameName.visible = False
            gameInfo.visible = False
            gameLevels.visible = False
            gameControls.visible = False
            gameStart.visible = False
            instructionStartLabel.visible = False
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

        elif gameControlHitbox.containsShape(cursor1) or gameControlHitbox.containsShape(cursor2):
            gameName.visible = False
            gameInfo.visible = False
            gameLevels.visible = False
            gameControls.visible = False
            gameStart.visible = False
            instructionStartLabel.visible = False
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
                rightControlLabel.visible = True
                leftControlLabel.visible = True
                pauseControlLabel.visible = True
                unpauseControlLabel.visible = True
                controlTestGround.visible = True
                controlTestPlayer.visible = True
                tryItNowLabel.visible = True
                app.playerControlMovement = True
                cutControlLabel.visible = True

        elif gameStartHitbox.containsShape(cursor1) or gameStartHitbox.containsShape(cursor2):
            gameName.visible = False
            gameInfo.visible = False
            gameLevels.visible = False
            gameControls.visible = False
            gameStart.visible = False
            instructionStartLabel.visible = False
            gameNameHitbox.visible = False
            gameInfoHitbox.visible = False
            gameLevelHitbox.visible = False
            gameControlHitbox.visible = False
            gameStartHitbox.visible = False
            app.startScreen = False
            app.mistyMeadows = True
            exitGameButtonLabel.visible = False
            if app.mistyMeadows:
                app.background = 'skyBlue'
                cursor1.visible = False
                cursor2.visible = False
                player1.visible = True
                level1Ground1.visible = True
                app.playerMovement = True
                level1Tree1.visible = True
                level1TreeLeaf11.visible = True
                level1TreeLeaf12.visible = True

    # Controls Pause Menu
    elif app.controlScreen:
        if controlPMenu4.containsShape(cursor1) or controlPMenu4.containsShape(cursor2):
            gameName.visible = True
            gameInfo.visible = True
            gameLevels.visible = True
            gameControls.visible = True
            gameStart.visible = True
            app.startScreen = True
            instructionStartLabel.visible = True
            app.backButtonEnabled = False
            backLabel.visible = False
            backLabelHitbox.visible = False
            LabelInfo1.visible = False
            LabelInfo2.visible = False
            LabelInfo3.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            infoLabelLevel.visible = False
            app.levelScreen = False
            rightControlLabel.visible = False
            leftControlLabel.visible = False
            pauseControlLabel.visible = False
            unpauseControlLabel.visible = False
            controlTestGround.visible = False
            controlTestPlayer.visible = False
            tryItNowLabel.visible = False
            app.controlScreen = False
            app.playerControlMovement = False
            controlPMenu1.visible = False
            controlPMenu2.visible = False
            controlPMenu3.visible = False
            controlPMenu4.visible = False
            app.pauseControlScreenActive = False
            cursor1.fill = 'white'
            cursor2.fill = 'white'
            cutControlLabel.visible = False
            app.mistyMeadows = False
            level1Tree1.visible = False
            level1TreeLeaf11.visible = False
            level1TreeLeaf12.visible = False
            app.pauseScreenActive = False
            level1Name.visible = False
            exitGameButtonLabel.visible = False

    elif app.mistyMeadows:
        if app.pauseScreenActive:
            if pauseMenu4.containsShape(cursor1) or pauseMenu4.containsShape(cursor2):
                gameName.visible = True
                gameInfo.visible = True
                gameLevels.visible = True
                gameControls.visible = True
                gameStart.visible = True
                app.startScreen = True
                instructionStartLabel.visible = True
                app.backButtonEnabled = False
                backLabel.visible = False
                backLabelHitbox.visible = False
                LabelInfo1.visible = False
                LabelInfo2.visible = False
                LabelInfo3.visible = False
                levelChooserLabel1.visible = False
                levelChooserLabel1Border.visible = False
                infoLabelLevel.visible = False
                app.levelScreen = False
                rightControlLabel.visible = False
                leftControlLabel.visible = False
                pauseControlLabel.visible = False
                unpauseControlLabel.visible = False
                controlTestGround.visible = False
                controlTestPlayer.visible = False
                tryItNowLabel.visible = False
                app.controlScreen = False
                app.playerControlMovement = False
                controlPMenu1.visible = False
                controlPMenu2.visible = False
                controlPMenu3.visible = False
                controlPMenu4.visible = False
                app.pauseControlScreenActive = False
                cursor1.fill = 'white'
                cursor2.fill = 'white'
                cursor1.visible = True
                cursor2.visible = True
                app.background = 'black'
                player1.visible = False
                level1Ground1.visible = False
                app.playerMovement = False
                pauseMenu1.visible = False
                pauseMenu2.visible = False
                pauseMenu3.visible = False
                pauseMenu4.visible = False
                pauseMenu5.visible = False
                cutControlLabel.visible = False
                app.mistyMeadows = False
                level1Tree1.visible = False
                level1TreeLeaf11.visible = False
                level1TreeLeaf12.visible = False
                app.pauseScreenActive = False
                level1Name.visible = False
                exitGameButtonLabel.visible = False

    elif app.levelScreen:
        if levelChooserLabel1Hitbox.containsShape(cursor1) or levelChooserLabel1Hitbox.containsShape(cursor2):
            gameName.visible = False
            gameInfo.visible = False
            gameLevels.visible = False
            gameControls.visible = False
            gameStart.visible = False
            instructionStartLabel.visible = False
            gameNameHitbox.visible = False
            gameInfoHitbox.visible = False
            gameLevelHitbox.visible = False
            gameControlHitbox.visible = False
            gameStartHitbox.visible = False
            app.startScreen = False
            app.mistyMeadows = True
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
            if app.mistyMeadows:
                app.background = 'skyBlue'
                cursor1.visible = False
                cursor2.visible = False
                player1.visible = True
                level1Ground1.visible = True
                app.playerMovement = True
                level1Tree1.visible = True
                level1TreeLeaf11.visible = True
                level1TreeLeaf12.visible = True


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
    elif app.mistyMeadows:
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

    if app.mistyMeadows:
        if key == 'p':
            app.playerMovement = False
            pauseMenu1.visible = True
            pauseMenu2.visible = True
            pauseMenu3.visible = True
            pauseMenu4.visible = True
            pauseMenu5.visible = True
            cursor1.visible = True
            cursor2.visible = True
            cursor1.toFront()
            cursor2.toFront()
            app.pauseScreenActive = True

        elif key == 'P':
            app.playerMovement = False
            pauseMenu1.visible = True
            pauseMenu2.visible = True
            pauseMenu3.visible = True
            pauseMenu4.visible = True
            pauseMenu5.visible = True
            cursor1.visible = True
            cursor2.visible = True
            cursor1.toFront()
            cursor2.toFront()
            app.pauseScreenActive = True

        elif key == 'u':
            app.playerMovement = True
            pauseMenu1.visible = False
            pauseMenu2.visible = False
            pauseMenu3.visible = False
            pauseMenu4.visible = False
            pauseMenu5.visible = False
            cursor1.visible = False
            cursor2.visible = False
            app.pauseScreenActive = False

        elif key == 'U':
            app.playerMovement = True
            pauseMenu1.visible = False
            pauseMenu2.visible = False
            pauseMenu3.visible = False
            pauseMenu4.visible = False
            pauseMenu5.visible = False
            cursor1.visible = False
            cursor2.visible = False
            app.pauseScreenActive = False

    if app.endGame:
        if key == 'r':
            gameName.visible = True
            gameInfo.visible = True
            gameLevels.visible = True
            gameControls.visible = True
            gameStart.visible = True
            app.startScreen = True
            instructionStartLabel.visible = True
            app.backButtonEnabled = False
            backLabel.visible = False
            backLabelHitbox.visible = False
            LabelInfo1.visible = False
            LabelInfo2.visible = False
            LabelInfo3.visible = False
            levelChooserLabel1.visible = False
            levelChooserLabel1Border.visible = False
            infoLabelLevel.visible = False
            app.levelScreen = False
            rightControlLabel.visible = False
            leftControlLabel.visible = False
            pauseControlLabel.visible = False
            unpauseControlLabel.visible = False
            controlTestGround.visible = False
            controlTestPlayer.visible = False
            tryItNowLabel.visible = False
            app.controlScreen = False
            app.playerControlMovement = False
            controlPMenu1.visible = False
            controlPMenu2.visible = False
            controlPMenu3.visible = False
            controlPMenu4.visible = False
            app.pauseControlScreenActive = False
            cursor1.fill = 'white'
            cursor2.fill = 'white'
            cursor1.visible = True
            cursor2.visible = True
            app.background = 'black'
            player1.visible = False
            level1Ground1.visible = False
            app.playerMovement = False
            pauseMenu1.visible = False
            pauseMenu2.visible = False
            pauseMenu3.visible = False
            pauseMenu4.visible = False
            pauseMenu5.visible = False
            cutControlLabel.visible = False
            app.mistyMeadows = False
            level1Tree1.visible = False
            level1TreeLeaf11.visible = False
            level1TreeLeaf12.visible = False
            gameFinishLabel.visible = False
            r2restartLabel.visible = False
            app.endGame = False
            player1.centerX = 0
            app.pauseScreenActive = False
            exitGameButtonLabel.visible = True
    elif key == 'R':
        gameName.visible = True
        gameInfo.visible = True
        gameLevels.visible = True
        gameControls.visible = True
        gameStart.visible = True
        app.startScreen = True
        instructionStartLabel.visible = True
        app.backButtonEnabled = False
        backLabel.visible = False
        backLabelHitbox.visible = False
        LabelInfo1.visible = False
        LabelInfo2.visible = False
        LabelInfo3.visible = False
        levelChooserLabel1.visible = False
        levelChooserLabel1Border.visible = False
        infoLabelLevel.visible = False
        app.levelScreen = False
        rightControlLabel.visible = False
        leftControlLabel.visible = False
        pauseControlLabel.visible = False
        unpauseControlLabel.visible = False
        controlTestGround.visible = False
        controlTestPlayer.visible = False
        tryItNowLabel.visible = False
        app.controlScreen = False
        app.playerControlMovement = False
        controlPMenu1.visible = False
        controlPMenu2.visible = False
        controlPMenu3.visible = False
        controlPMenu4.visible = False
        app.pauseControlScreenActive = False
        cursor1.fill = 'white'
        cursor2.fill = 'white'
        cursor1.visible = True
        cursor2.visible = True
        app.background = 'black'
        player1.visible = False
        level1Ground1.visible = False
        app.playerMovement = False
        pauseMenu1.visible = False
        pauseMenu2.visible = False
        pauseMenu3.visible = False
        pauseMenu4.visible = False
        pauseMenu5.visible = False
        cutControlLabel.visible = False
        app.mistyMeadows = False
        level1Tree1.visible = False
        level1TreeLeaf11.visible = False
        level1TreeLeaf12.visible = False
        gameFinishLabel.visible = False
        r2restartLabel.visible = False
        app.endGame = False
        player1.centerX = 0
        app.pauseScreenActive = False
        exitGameButtonLabel.visible = True


cmu_graphics.run()
