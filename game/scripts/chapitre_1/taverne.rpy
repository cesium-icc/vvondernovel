label c1_taverne:
    mct "..."
    mct "Ah ma tête..."
    mct "Qu'est-ce qui s'est passé ?"
    "[player] se retrouva attaché à une chaise, mains liées."
    mct "Depuis quand est-ce que... Et où suis-je ?"
    scene taverne
    show halfblack zorder 100
    with Dissolve(.5)
    play music dark_tavern
    "[player] se réveilla dans une taverne peu éclairée."
    show chawas at truecenter with Dissolve(.5)
    "Il était entourée de formes fantomatiques, d'une taille semi-humaine."
    "Une silhouette, de taille humaine, sorti de la foule, en émettant un son strident."
    show pawa
    p """
    Sheeeeeeeeeeeeeeeeeeeesh !

    Salut et bienvenue sur le territoire des Chawas !

    Je suis Pawa, maîtresse de ces lieux.
    """ (name="???")

    p """
    Tu te demandes sûrement pourquoi tu es attaché.

    Eh bien, la réponse est simple, ici il y a une chose qu'on ne tolère pas...
    """

    show pawa yandere
    p "Les voleurs de bouffe !"

    mc "Les voleurs de... Il y a un malentendu ! C'est moi à qui on a volé un poisson !"

    p "Ne fait pas l'innocent, on t'a vu monter l'escalier et voler l'offrande posé sur mon autel !"

    mc "Certes, mais je peux tout expl..."

    p "Tsssst, je ne veux rien savoir. Ton destin est tracé d'avance !"

    p "Nous allons te découper et te transformer en pâtée pour Chawa !"

    chs "OUI ! DE LA PÂTÉE POUR CHAWA !"

    p "Et afin de déterminer le temps de cuisson, nous allons analyser tes affaires et déterminé à quel point tu es maléfique."

    mc "Mais je vous dit que je..."

    p "SILENCE ! Qu'on apporte les pièces à convictions !"

    "Une forme fantomatique s'approcha avec le sac de [player], ainsi que son épée."

    ch "Première pièce à conviction : une épée !"

    p "Ah, donc en plus d'un voleur, nous sommes en face d'un assassin !"

    mc "Il y a erreur : je suis aventurier, et cette épée est mon arme !"

    p "Un... aventurier ?"

    chs "HAHAHAHA !"

    p "Quel genre d'aventurier est épuisé après avoir monté quarante petites marches ?"

    mc "Oui bah je suis un aventurier {i}débutant{/i} !
    Et puis vu en contre-plongée on avait l'impression qu'il y en avait au moins sept mille..."

    show pawa

    p """
    Non mais oh, dit que mon autel est mal situé pendant que t'y es !

    Tu sais combien ça coûte de construire un escalier en pierre au beau milieu de la forêt ?

    Sans compter les fausses toiles d'araignée pour donner un côté ancien à l'arche d'entrée !
    Quelle galère ça a été de trouver un artisan qui sache faire ça !
    """

    show pawa yandere

    p "Bref, pièce à conviction suivante !"

    "Le chawa fouilla dans le sac de [player]."

    ch "Un giga-tacos !"

    p "Un giga-tac..."
    p "..."

    show pawa
    stop music

    p "J'accepte ton offrande, tu es épargné."
    mc "... Pardon ?"
    p "Tu es épargné : Tu as essayé de voler un poisson. Donc si tu m'offres ton giga-tacos, on est quitte niveau matériel."
    p "Et pour l'affront que tu m'as fait, il suffit que tu deviennes mon esclave pour les deux prochains siècles et
    ça devrait suffire."
    mct "Ouf, je suis sauvé. Je dois juste la servir pour deux siè... attends, quoi ?"
    mc "Deux siècles de servitude, mais ça va pas ou quoi ??? Juste pour un malheureux poisson ?"
    show pawa yandere
    play music dark_tavern
    p "Peut-être préfères-tu la première option ?"
    chs "LA PÂTÉE POUR CHAWA !"
    stop music
    mc "Ok, ok, j'accepte ton marché."
    show pawa
    p "Parfait ! Détachez-le !"
    "[player] s'étira, laissant son sang circuler dans ses bras et poignées tout juste déliés."
    p "Et ouvrez les fenêtres, ça commence à sentir la transpi de Chawa ici !"
    hide halfblack with Dissolve(.5)
    play music holy_music
    "Pawa sortit une flûte et la tendit vers [player]."
    p "Je te présente la Sainte Flûte. Si tu fais une promesse en la tenant, et que tu la romps,
    tu seras transformé en burger."
    mct "*Glurp*"
    "Pawa et [player] prirent chacun un côté de l'instrument, et commencèrent le sermon."
    p "Promets-tu de me jurer fidélité, et d'obéir à chacun de mes ordres, pour les deux cents prochaines années ?"
    mc "Je le promets."
    p "Promets-tu de défendre bec et ongles ma vie ainsi que mes possessions, pour les deux cents prochaines années ?"
    mc "Je le promets."
    p "Promets-tu de me donner le giga-tacos que contenait ton sac ?"
    mc "..."
    mc "Je le promets."
    "Pawa retira la flûte des mains de [player]"
    p "Aujourd'hui, je te déclare officiellement Chawa d'Honneur."
    stop music fadeout 1
    "Ce soir, bière pour tout le monde !"
    chs "HOURA !!!"
    play music tavern fadein 1
    hide pawa with Dissolve(.5)
    hide chawas with Dissolve(.5)
    "Les chawas se mirent à se servir en alcool. En {i}beaucoup{/i} d'alcool."
    "Avec Pawa, ils chantèrent une chanson de bienvenue à leur nouvel ami."
    chs "AMI [player!u] ! {size=-5}AMI [player!u] !{/size} LÈVE TON VERRE !
    ET SURTOUT, NE LE RENVERSE PAS !" (name="Pawa & Les Chawas")
    "Ce soir fut une soirée de fête."
    "Et ils mangèrent beaucoup de viande."
    "C'est ainsi que commença l'aventure de [player]."
    "Pour voir la suite, veuillez acheter le DLC à 999.99 € sur Steam."
    "Et pour vous mettre l'eau à la bouche, une scène post-générique..."
    stop music fadeout 1
    scene black with Dissolve(1.5)
    jump c1_popo_castle