from gi.repository import Tracker

def search(search_term):
    query = Tracker.SparqlQuery.new_for_string(
        f"SELECT ?urn WHERE {{ ?urn a nfo:FileDataObject ; nfo:fileName '*{search_term}*' . }}"
    )
    sparql_connection = Tracker.SparqlConnection.get_default()
    sparql_connection.query(query, None, tracker_search_cb)

def tracker_search_cb(query, result, user_data):
    while result.next():
        uri = result.get_string(0)
        print(uri)

search('uml_uzum.jpg')
