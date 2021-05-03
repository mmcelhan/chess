import tinydb
import os
import helpers as hlp
import file_drop
import dropdown_menu


if __name__ == '__main__':
    db = tinydb.TinyDB(os.path.join('db', 'db.json'))

    file_drop_instance = file_drop.WindowFileDropApp()
    file_drop_instance.run()
    pgn_json = file_drop_instance.json_dict

    hlp.reset()
    dropdown_menu_instance = dropdown_menu.PrimaryRootCauseDropdownApp()
    dropdown_menu_instance.run()

    primary_root_cause = dropdown_menu_instance.primary_root_cause

    pgn_json['primary_root_cause'] = primary_root_cause

    print(pgn_json)
    query = tinydb.Query()
    
    db.upsert(pgn_json, ((query.Date == pgn_json['Date'])
                         & (query.White == pgn_json['White'])
                         & (query.WhiteElo == pgn_json['WhiteElo'])))
