"""
EXAMPLE OF USING keyboards.py

def paginated_hometasks(on_click):
    return ScrollingGroup(
        Select(
            Format('{item[is_completed]} {item[date]} - {item[lesson]}'),
            id='s_scroll_hometasks',
            item_id_getter=operator.itemgetter('uuid'),
            items='hometasks',
            on_click=on_click
        ),
        id='hometasks_id',
        width=1, height=5
    )
"""