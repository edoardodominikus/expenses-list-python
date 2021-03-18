class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        """Declare categories listed """
        self._categories=['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    def view(self):
        """ This method is for printing the categories listed"""
        def view_categories(categories,prefix=()):
            if type(categories) is list:
                i = 0
                for item in categories:
                    if type(item) is not list:
                        i += 1
                    view_categories(item,prefix+(i,))
            else:
                s = ' '*(len(prefix)-1)
                s += '-' + categories
                print(s)
                
        view_categories(self._categories,prefix=())

    def is_category_valid(self,category):
        """ This method is for checking if the input given is in the list categories declared"""
        def category_valid(categories,category):
                    if type(categories) is list:
                        for i,v in enumerate(categories):
                            p = category_valid(v,category)
                            if p == True:
                                return True
                            if p != False:
                                return False
                    return categories == category
        return category_valid(self._categories,category)



    def find_subcategories(self, category):
        """ This method is for returning the category in input category under input"""
        def find_subcategories_gen(category, categories, found=False):
          if type(categories) == list:
           for index, child in enumerate(categories):
            yield from find_subcategories_gen(category, child,found)
            if child == category and index + 1 < len(categories) and type(categories[index + 1]) == list and found == False:
                # When the target category is found,
                # recursively call this generator on the subcategories
                # with the flag set as True.
                yield from find_subcategories_gen(category,categories[index:index+2],found = True)

          else:
           if categories == category or found == True:
            yield categories
        return [i for i in find_subcategories_gen(category, self._categories)]