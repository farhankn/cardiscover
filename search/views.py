from car.models import carName

from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import re
# Create your views here.

from django.shortcuts import render,render_to_response


def normalize_query(
		    query_string,
		    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub
                    ):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query



                    		    
#@login_required(login_url='/login/')   #uncomment after user login enabled
def search(request):

    	
    	query_string = ''
    	found_entries = None
    	if ('q' in request.GET) and request.GET['q'].strip():
        	query_string = request.GET['q']
        
       		entry_query = get_query(query_string, ['name','Manufacturer','description','engine','fueltype','bodytype',])
        
        	found_entries = carName.objects.filter(entry_query).order_by('-last_updated')

    	return render_to_response('searchresults.html',
                       		  { 
                      		   'query_string': query_string, 
                     		    'found_entries': found_entries 
                     		    	  },
                     		    context_instance=RequestContext(request))
                    		    

def msearch(request):

	if ('carbrand' in request.GET) and request.GET['carbrand'].strip():
        	cbrand = request.GET['carbrand']
	if ('carmodel' in request.GET) and request.GET['carmodel'].strip():
        	cmodel = request.GET['carmodel']
	if ('pricemin' in request.GET) and request.GET['pricemin'].strip():
        	cminprice = request.GET['pricemin']
	if ('pricemax' in request.GET) and request.GET['pricemax'].strip():
        	cmaxprice = request.GET['pricemax']    	

    # da farhane   vvvvv
    # HAVE TO FURTHER MODIFY THE FILTER TO FILTER MIN PRICE MODEL AND PRICE RANGE AFTER MODELS IS SET right, NOW JUST TEMP!!!!!!! 

	bcar = carName.objects.filter(Manufacturer = cbrand).order_by('-last_updated')

	return render_to_response('searchresults.html',
                       		  { 
                      		   'query_string': bcar, 
                     		    'found_entries': bcar, 
                     		    	  },
                     		    context_instance=RequestContext(request))





