label entry_sanctuary:
    """
    Il le poursuivi jusqu'au moment où l'animal entra à l'orée d'une forêt.

    Notre aventurier s'arrêta un instant, reprenant son souffle. Et en profita pour contempler l'entrée de la forêt.
    """
    show forest entry at truecenter with moveinbottom
    """
    C'était une arche. Son bois était couvert de toiles d'araignées. Et derrière elle se trouvait un escalier montant.

    Typiquement le genre d'escalier menant à un sanctuaire situé derrière sept milles marches...
    
    Essuyant la sueur sur son front, [player] se demanda si ça en valait la peine.
    """
label entry_sanctuary_choice:
    menu:
        "C'EST MON POISSON !":
            "[player] reprit ses esprits. Ce n'était pas n'importe quel poisson, c'était {i}son{/i} poisson."
            "Débranchant son cerveau, il monta à toute hâte les sept milles marches menant au précieux met."
            jump sanctuary
        "Ça va aller, ce n'est qu'un poisson...":
            "[player] voulait reprendre son met, mais la fatigue avait enchaîné ses jambes à la terre."
            "Il rebroussa chemin..."
            jump vers_le_royaume_popo