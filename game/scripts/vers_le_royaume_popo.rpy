label vers_le_royaume_popo:
    scene popo_castle with Dissolve(0.5)
    mct "Le Royaume Popo..."
    scene before_momo_step with Dissolve(0.5)
    mct "Enfin ma nouvelle vie va commencer..."
    stop music
    show momo_step
    "CRASH !"        
    show momo_step at momo_scroll
    pause
    "GAME OVER"
    menu:
        "Revenir devant l'entrée de la forêt.":
            scene start
            show forest entry at truecenter
            with Dissolve (.5)
            play music start_music
            jump entry_sanctuary_choice
        "Revenir au menu principal":
            return