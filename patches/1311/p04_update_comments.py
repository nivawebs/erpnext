# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

def execute():
	import webnotes
	for name in webnotes.conn.sql_list("""select name from tabComment"""):
		webnotes.get_obj("Comment", name).update_comment_in_doc()
	