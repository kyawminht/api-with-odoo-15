

from odoo.http import request, Response
from odoo import http
import json

class SchoolController(http.Controller):
    # GET ALL SCHOOLS
    @http.route('/api/school', auth='public', type='json', methods=['GET'], csrf=False)
    def get_schools(self, **kwargs):
        try:
            schools = request.env['school.school'].sudo().search([])
            data = [{
                'id': school.id,
                'name': school.name,
                'address': school.address
            } for school in schools]

            return {'data':data}
        except Exception as e:
            return Response(
                json.dumps({'error': str(e)}),
                content_type='application/json',
                status=500
            )

    @http.route('/api/school', auth='public', type='json', methods=['POST'], csrf=False)
    def create_school(self, **kwargs):
        try:
            data = request.jsonrequest

            # Check if 'name' is missing
            if not data.get('name'):
                return {
                    'error': 'Name is required'
                }  # Correct indentation

            # Proper indentation for the next line
            school = request.env['school.school'].sudo().create({
                'name': data.get('name'),
                'address': data.get('address')
            })

            # Return the created school details
            return {
                'message':'new data created',
                'id': school.id,
                'name': school.name,
                'address': school.address
            }
        except Exception as e:
            return {
                'error': str(e)
            }

    @http.route('/api/school/<int:id>', auth='public', type='json', methods=['PUT'], csrf=False)
    def update_school(self, id, **kwargs):
        school=request.env['school.school'].sudo().browse(id)
        if not school.exists:
            return {
                'error':'school not found'
            }
        data=request.jsonrequest
        school.write({
            'name':data.get('name',school.name),
            'address':data.get('address',school.address)
        })
        return {
            'message':'school updated successfully',
            'status':200
        }

    @http.route('/api/school/<int:id>', auth='public', type='json', methods=['DELETE'], csrf=False)
    def delete_school(self, id, **kwargs):
        school=request.env['school.school'].sudo().browse(id)
        if not school.exists:
            return {
                'error':'school not found'
            }
        school.unlink()
        return {
            'message':'school deleted'
        }

    @http.route('/api/school/<int:id>', auth='public', type='json', methods=['GET'], csrf=False)
    def show_school(self, id, **kwargs):
        school=request.env['school.school'].sudo().browse(id)
        if not school.exists():
            return {
                'message': "school not found"
            }
        school_data={
            'id':school.id,
            'name':school.name,
            'address':school.address
        }
        return {'data':school_data}