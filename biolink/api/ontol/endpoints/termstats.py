import logging

from flask import request
from flask_restplus import Resource
from biolink.api.restplus import api
from biogolr.golr_associations import calculate_information_content
import pysolr

log = logging.getLogger(__name__)

ns = api.namespace('ontol', description='foo bar')

parser = api.parser()
parser.add_argument('evidence', help="""Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)
                    or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.
                    """)

@ns.route('/information_content/<subject_category>/<object_category>/<subject_taxon>')
class InformationContentResource(Resource):

    @api.expect(parser)
    def get(self, subject_category, object_category, subject_taxon):
        """
        Calculates information content
        """
        args = parser.parse_args()
        return calculate_information_content(subject_category=subject_category,
                                             object_category=object_category,
                                             subject_taxon=subject_taxon,
                                             **args)


    
    

