label c1_entry_sanctuary:
    """
    Il le poursuivi jusqu'au moment où l'animal entra à l'orée d'une forêt.

    Notre aventurier s'arrêta un instant, reprenant son souffle. Et en profita pour contempler l'entrée de la forêt.
    """
    show forest entry at truecenter with moveinbottom
    """
    C'était une arche. Son bois était couvert de toiles d'araignées. Et derrière elle se trouvait un escalier montant.

    Typiquement le genre d'escalier menant à un sanctuaire situé derrière sept milles marches...
    
    Essuyant la sueur sur son front, [player] se demanda si ça en valait la peine.

    Il se remémora alors des paroles de son grand-père.
    """

    show grandpa at truecenter with Dissolve(.5)
    "Grand-père" "Souviens toi de pardonner les autres. Le pardon est la plus douce sensation pour nôtre âme."
    hide grandpa with Dissolve(.5)

    "Cependant, l'esprit de [player] était voilé par la rancœur. Pardonner le voleur lui emblait inconcevable.
    Par contre il concevait parfaitement le point du côté qu'il aurait une fois les escaliers gravis."

label c1_entry_sanctuary_choice:
    menu:
        "C'EST MON POISSON !":
            "[player] reprit ses esprits. Ce n'était pas n'importe quel poisson, c'était {i}son{/i} poisson."
            "Débranchant son cerveau, il monta à toute hâte les sept milles marches menant au précieux met."
            jump c1_sanctuary
        "Pardonner.":
            "[player] pardonna le félin."
            "Il sentit son cœur s'alléger, et rebroussa chemin."
            jump c1_entry_popo_kingdom
        "Je le laisse filer pour l'instant. Mais un jour je me vengerai !":
            "[player] voulait reprendre son met, mais la fatigue avait enchaîné ses jambes à la terre."
            "Il rebroussa chemin..."
            jump c1_momosaure