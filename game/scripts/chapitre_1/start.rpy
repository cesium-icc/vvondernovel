label start :
    $player = "Jean-Player"
    play music start_music fadein 3.0
    scene start with Dissolve (3)
    "Dans un monde lointain, très lointain, au delà de tout ce que vous connaissez,"
    "Vivait un jeune homme, du nom de [player]."
    show mc with Dissolve(1.5)
    """
    Il est né dans un petit village au pied d'une montagne.
    En été comme en hivers, l'air frais le revigorait chaque matin,
    lui et sa famille, depuis cent générations.

    Il était heureux, mais il ressentait comme un manque. Ce manque se transforma peu à peu en lassitude quotidienne.

    Un jour, il décida alors de quitter son village pour partir...

    ... à l'aventure !
    """
    mct """
    Le Royaume Popo n'est plus bien loin maintenant.
    J'ai entendu dire qu'il y a toutes sortes de guildes d'aventuriers là-bas.
    
    Allez, en avant toute...
    """

    play sound stomach_empty
    "Estomac" "*GARGOUILLEMENTS DE GROS CHAD*"
    mct """
    ...

    Bon, d'abord, c'est l'heure du second petit dej'.
    """
    hide mc with Dissolve(.5)
    """
    [player] s'assit et sur l'herbe, et pris un morceau de pain.

    Quand tout à coup, ...
    """
    show cat stealing at truecenter with moveinbottom
    "... il aperçu un chat, fouillant dans son sac."
    hide cat stealing with moveoutbottom
    play sound run_grass
    """
    Quand le félin s'aperçut qu'il était repéré, il déguerpit aussitôt, emportant son butin avec lui.
    
    [player] se mit alors à courir après le petit voleur.
    """
    jump c1_entry_sanctuary
    


