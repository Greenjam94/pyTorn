class urls:
    def __init__(self):
        self.base = 'https://api.torn.com/'

        # Torn UI
        self.attack = 'https://www.torn.com/loader2.php?sid=getInAttack&user2ID={target}'.format(target="{target}")

        # User
        """
        Notes:
        - User ID not required when requesting the key's owner data.
        - Accepts comma separated selections.
        - 'from' and 'to' UNIX timestamps can be passed to filter some selections
        """
        self.user = 'user/{id}?selections={fields}'.format(id="{id}", fields="{fields}")

        # Property
        self.property = 'property/{id}?selections={fields}'.format(id="{id}", fields="{fields}")

        # Faction
        """
        Notes:
        - Faction ID not required when requesting the key's owner data.
        - Accepts comma separated selections.
        - 'from' and 'to' UNIX timestamps can be passed to filter some selections.
        - The 'contributors' selection requires the inclusion of the stat name (I.e. &stat=busts)
        """
        self.faction = 'faction/{id}?selections={fields}'.format(id="{id}", fields="{fields}")


        # Company
        """
        Notes:
        - Company ID not required when requesting the key's owner data.
        - Accepts comma separated selections.
        """
        self.company = 'company/{id}?selections={fields}'.format(id="{id}", fields="{fields}")


        # Market
        """
        Notes: Accepts comma separated selections.
        """
        self.market = 'market/{id}?selections={fields}'.format(id="{id}", fields="{fields}")

        # Generic
        """
        Notes: Accepts comma separated selections.
        """
        self.generic = 'torn/{id}?selections={fields}'.format(id="{id}", fields="{fields}")

    def base(self):
        return self.base

    def get_attack(self):
        return self.attack

    def get_user(self):
        return self.base + self.user

    def get_property(self):
        return self.base + self.property
    
    def get_faction(self):
        return self.base + self.faction
    
    def get_company(self):
        return self.base + self.company

    def get_market(self):
        return self.base + self.market
    
    def get_generic(self):
        return self.base + self.generic
