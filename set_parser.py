import json


def deref(li):
    if len(li) == 1:
        it = li[0]

        if type(it) == str:
            return '"' + it + '"'
        else:
            return it
    else:
        return li


class Pokemon:
    def __init__(self):
        # List of strings
        self.item = []

        # List of strings
        self.ability = []

        # Object = {hp,atk,def,spa,spd,spe}
        self.evs = []

        # Object = {hp,atk,def,spa,spd,spe}
        self.ivs = []

        # Strings
        self.nature = []

        # List of Strings and lists of strings
        self.moves = []

    def from_ps(self, ps):

        # EXPECTED ORDER / FORMAT:
        # 1. SPECIES @ ITEM 1 / ITEM 2 / ...
        # 2. Ability: ABILITY 1 / ABILITY 2 / ...
        # 3. EVs: x HP / y Atk / ...
        # 4. IVs: x HP / y Atk / ...
        # 5. NATURE 1 / NATURE 2 Nature
        # 6. - MOVE 1 / ALT MOVE 1 / ...
        # 7. - MOVE 2 / ALT MOVE 2 / ...
        # 8. - MOVE 3 / ALT MOVE 3 / ...
        # 9. - MOVE 4 / ALT MOVE 4 / ...

        # Species, returned for indexing
        species = None

        # MOVES
        self.moves = []

        # Record current line
        lineno = 0

        try:

            for p in ps:
            
                # Increment line counter
                lineno += 1

                p = p.lower()

                if '@' in p:
                    # 1. SPECIES @ ITEM 1 / ITEM 2 / ...
                    line = p.split('@')[1]
                    self.item = []

                    for i in line.split('/'):
                        self.item.append(i.strip())

                    # Handling first half (nickname / species)
                    species = p.split('@')[0].strip()

                elif 'ability:' in p:
                    # 2. Ability: ABILITY 1 / ABILITY 2 / ...
                    line = p.split(':')[1].strip()
                    self.ability = []

                    for a in line.split('/'):
                        self.ability.append(a.strip())

                elif 'evs:' in p:
                    # 3. EVs: x HP / y Atk / ...
                    line = p.split(':')[1]
                    self.evs = [{}]

                    for e in line.split('/'):
                        t = e.strip().lower().split(' ')

                        self.evs[0][t[1].strip()] = t[0].strip()

                elif 'ivs:' in p:
                    # 4. IVs: x HP / y Atk / ...
                    line = p.split(':')[1]
                    self.ivs = [{}]

                    for i in line.split('/'):
                        t = i.strip().lower().split(' ')

                        self.ivs[0][t[1].strip()] = t[0].strip()

                elif '- ' in p:
                    line = p.replace('- ', '').strip()

                    opt = []

                    for m in line.split('/'):
                        opt.append(m.strip())

                    self.moves.append(opt)

                # 5. NATURE 1 / NATURE 2 Nature
                elif 'nature' in p:
                    line = p.lower().replace('nature', '').strip()

                    self.nature = []

                    for n in line.split('/'):
                        self.nature.append(n.strip())

            return species.replace('-', '').replace(' ', '')

        # If program fails, return line number and line failed on
        except Exception as e:
            
            # If there are any lines
            if len(ps):
                # Return lineno, line content
                return [lineno,ps[lineno-1]]
                
            # No lines at all
            else:
                # Return that there is no content
                return [0,'']
        
            

    def to_hash(self):
        return {
            "item": self.item,
            "ability": self.ability,
            "evs": self.evs,
            "ivs": self.ivs,
            "nature": self.nature,
            "moves": self.moves,
        }

    def __str__(self):
        return json.dumps(self.to_hash())

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    landorus = Pokemon()

    landorus.item.append("Choice Scarf")
    landorus.item.append("Assault Vest")

    landorus.ability.append("Intimidate")

    landorus.evs.append({"hp": 4, "atk": 244, "def": 4, "spd": 4, "spe": 252})
    landorus.ivs.append({"hp": 31, "atk": 31, "def": 31, "spd": 31, "spe": 31})

    landorus.nature.append("Adamnant")
    landorus.nature.append("Jolly")

    landorus.moves.append("Rock Slide")
    landorus.moves.append("Earthquake")
    landorus.moves.append(["Superpower", "Knock Off"])
    landorus.moves.append("U-Turn")

    read = Pokemon()

    set = [
        'Landorus-Therian @ Choice Scarf / Assault Vest',
        'Ability: Intimidate',
        'EVs: 4 HP / 244 Atk / 4 Def / 4 SpD / 252 Spe',
        'Adamant / Jolly Nature',
        '- Earthquake',
        '- Rock Slide',
        '- U-turn',
        '- Superpower / Knock Off']

    read.from_ps(set)
    print(read)
