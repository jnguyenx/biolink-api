import logging

from flask import request
from flask_restplus import Resource
from biolink.datamodel.serializers import association
from biolink.api.restplus import api
import pysolr

log = logging.getLogger(__name__)

ns = api.namespace('ontol/slimmer', description='foo bar')

parser = api.parser()
#parser.add_argument('subject_taxon', help='SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default')

@ns.route('/<subset>')
class Foo(Resource):

    @api.expect(parser)
    @api.marshal_list_with(association)

    @api.expect(parser)
    @api.marshal_list_with(association)
    def get(self, subset):
        """
        Maps to slim
        """
        args = parser.parse_args()

        return []


    
    

