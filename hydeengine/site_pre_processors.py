import sys
from hydeengine.siteinfo import ContentNode
from django.conf import settings
from hydeengine.file_system import Folder
from siteinfo import SiteNode

"""
    PRE PROCESSORS
    
    Can be launched before the parsing of each templates and
    after the loading of site info.
"""

class CategoriesManager:   
    
    """
    Fetch the category(ies) from every post under the given node
    and creates a reference on them in CONTEXT and the node.
    """
    @staticmethod
    def process(folder, params):
        context = settings.CONTEXT
        site = context['site']    
        node = params['node'] 
        categories = {}                                      
        for post in node.walk_pages():           
            if hasattr(post, 'categories') and post.categories != None:
                for category in post.categories:
                    if categories.has_key(category) == False:
                        categories[category] = set()
                    categories[category].add(post)     
        context['categories'] = categories 
        node.categories = categories