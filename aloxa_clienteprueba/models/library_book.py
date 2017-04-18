# -*-coding:utf-8 -*-

from openerp import models, fields

class LibraryBook(models.Model):
	_name = 'library.book'

	name = fields.Char('Title', required=True)
	date_realease = fields.Date('Date Release')
	notes = fields.Text('Internal Notes')
	description = fields.Text('Description')
	cover = fields.Binary('Book Cover')
	pages = fields.Integer(string = 'Number of Pages')
	reading_rating = fields.Float('Reader Average Rating')
	state = fields.Selection(
		[('draft','Not Avaliable'),
		('avaliable','Avaliable'),
		('lost','Lost')],
		'State')
	
