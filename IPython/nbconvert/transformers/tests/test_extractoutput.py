"""
Module with tests for the extractoutput transformer
"""

#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from .base import TransformerTestsBase
from ..extractoutput import ExtractOutputTransformer


#-----------------------------------------------------------------------------
# Class
#-----------------------------------------------------------------------------

class TestExtractOutput(TransformerTestsBase):
    """Contains test functions for extractoutput.py"""

    def test_constructor(self):
        """Can a ExtractOutputTransformer be constructed?"""
        transformer = ExtractOutputTransformer()
        transformer.enabled = True
        return transformer
    

    def test_output(self):
        """Test the output of the ExtractOutputTransformer"""
        nb, res = self.test_constructor()(self.build_notebook(), {})

        # Check if text was extracted.
        assert 'text_filename' in nb.worksheets[0].cells[0].outputs[1]
        text_filename = nb.worksheets[0].cells[0].outputs[1]['text_filename']

        # Check if png was extracted.
        assert 'png_filename' in nb.worksheets[0].cells[0].outputs[6]
        png_filename = nb.worksheets[0].cells[0].outputs[6]['png_filename']

        # Make sure an entry to the resources was added.
        assert 'outputs' in res

        # Verify text output
        assert text_filename in res['outputs']
        self.assertEqual(res['outputs'][text_filename], 'b')

        # Verify png output
        assert png_filename in res['outputs']
        self.assertEqual(res['outputs'][png_filename], 'g')
