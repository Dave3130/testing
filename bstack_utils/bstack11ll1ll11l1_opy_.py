# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1llll1l_opy_
logger = logging.getLogger(__name__)
class bstack11ll1ll1ll1_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll111ll11_opy_ = urljoin(builder, bstack11l1l11_opy_ (u"ࠧࡪࡵࡶࡹࡪࡹࠧᛇ"))
        if params:
            bstack11ll111ll11_opy_ += bstack11l1l11_opy_ (u"ࠣࡁࡾࢁࠧᛈ").format(urlencode({bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᛉ"): params.get(bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᛊ"))}))
        return bstack11ll1ll1ll1_opy_.bstack11ll111l1l1_opy_(bstack11ll111ll11_opy_)
    @staticmethod
    def bstack11ll11l1lll_opy_(builder,params=None):
        bstack11ll111ll11_opy_ = urljoin(builder, bstack11l1l11_opy_ (u"ࠫ࡮ࡹࡳࡶࡧࡶ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠬᛋ"))
        if params:
            bstack11ll111ll11_opy_ += bstack11l1l11_opy_ (u"ࠧࡅࡻࡾࠤᛌ").format(urlencode({bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᛍ"): params.get(bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᛎ"))}))
        return bstack11ll1ll1ll1_opy_.bstack11ll111l1l1_opy_(bstack11ll111ll11_opy_)
    @staticmethod
    def bstack11ll111l1l1_opy_(bstack11ll111ll1l_opy_):
        bstack11ll11l1111_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᛏ"), os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᛐ"), bstack11l1l11_opy_ (u"ࠪࠫᛑ")))
        headers = {bstack11l1l11_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᛒ"): bstack11l1l11_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᛓ").format(bstack11ll11l1111_opy_)}
        response = requests.get(bstack11ll111ll1l_opy_, headers=headers)
        bstack11ll1111lll_opy_ = {}
        try:
            bstack11ll1111lll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛔ").format(e))
            pass
        if bstack11ll1111lll_opy_ is not None:
            bstack11ll1111lll_opy_[bstack11l1l11_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛕ")] = response.headers.get(bstack11l1l11_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛖ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll1111lll_opy_[bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛗ")] = response.status_code
        return bstack11ll1111lll_opy_
    @staticmethod
    def bstack11ll1l1ll1l_opy_(bstack11ll111llll_opy_, data):
        logger.debug(bstack11l1l11_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡓࡧࡴࡹࡪࡹࡴࠡࡨࡲࡶࠥࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࠧᛘ"))
        return bstack11ll1ll1ll1_opy_.bstack11ll11l111l_opy_(bstack11l1l11_opy_ (u"ࠫࡕࡕࡓࡕࠩᛙ"), bstack11ll111llll_opy_, data=data)
    @staticmethod
    def bstack11ll1l1ll11_opy_(bstack11ll111llll_opy_, data):
        logger.debug(bstack11l1l11_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡕࡩࡶࡻࡥࡴࡶࠣࡪࡴࡸࠠࡨࡧࡷࡘࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡷࠧᛚ"))
        res = bstack11ll1ll1ll1_opy_.bstack11ll11l111l_opy_(bstack11l1l11_opy_ (u"࠭ࡇࡆࡖࠪᛛ"), bstack11ll111llll_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l111l_opy_(method, bstack11ll111llll_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11l1111_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛜ"), bstack11l1l11_opy_ (u"ࠨࠩᛝ"))
        headers = {
            bstack11l1l11_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛞ"): bstack11l1l11_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛟ").format(bstack11ll11l1111_opy_),
            bstack11l1l11_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛠ"): bstack11l1l11_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛡ"),
            bstack11l1l11_opy_ (u"࠭ࡁࡤࡥࡨࡴࡹ࠭ᛢ"): bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᛣ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1llll1l_opy_ + bstack11l1l11_opy_ (u"ࠣ࠱ࠥᛤ") + bstack11ll111llll_opy_.lstrip(bstack11l1l11_opy_ (u"ࠩ࠲ࠫᛥ"))
        try:
            if method == bstack11l1l11_opy_ (u"ࠪࡋࡊ࡚ࠧᛦ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack11l1l11_opy_ (u"ࠫࡕࡕࡓࡕࠩᛧ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack11l1l11_opy_ (u"ࠬࡖࡕࡕࠩᛨ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack11l1l11_opy_ (u"ࠨࡕ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡍ࡚ࡔࡑࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࡿࢂࠨᛩ").format(method))
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹࡪࡹࡴࠡ࡯ࡤࡨࡪࠦࡴࡰࠢࡘࡖࡑࡀࠠࡼࡿࠣࡻ࡮ࡺࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧᛪ").format(url, method))
            bstack11ll1111lll_opy_ = {}
            try:
                bstack11ll1111lll_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack11l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧ᛫").format(e, response.text))
            if bstack11ll1111lll_opy_ is not None:
                bstack11ll1111lll_opy_[bstack11l1l11_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪ᛬")] = response.headers.get(
                    bstack11l1l11_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫ᛭"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll1111lll_opy_[bstack11l1l11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᛮ")] = response.status_code
            return bstack11ll1111lll_opy_
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᛯ").format(e, url))
            return None
    @staticmethod
    def bstack11ll111l111_opy_(bstack11ll111ll1l_opy_, data):
        bstack11l1l11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡪࡴࡤࡴࠢࡤࠤࡕ࡛ࡔࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᛰ")
        bstack11ll11l1111_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛱ"), bstack11l1l11_opy_ (u"ࠨࠩᛲ"))
        headers = {
            bstack11l1l11_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛳ"): bstack11l1l11_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛴ").format(bstack11ll11l1111_opy_),
            bstack11l1l11_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛵ"): bstack11l1l11_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛶ")
        }
        response = requests.put(bstack11ll111ll1l_opy_, headers=headers, json=data)
        bstack11ll1111lll_opy_ = {}
        try:
            bstack11ll1111lll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛷ").format(e))
            pass
        logger.debug(bstack11l1l11_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࡖࡶ࡬ࡰࡸࡀࠠࡱࡷࡷࡣ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᛸ").format(bstack11ll1111lll_opy_))
        if bstack11ll1111lll_opy_ is not None:
            bstack11ll1111lll_opy_[bstack11l1l11_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩ᛹")] = response.headers.get(
                bstack11l1l11_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪ᛺"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll1111lll_opy_[bstack11l1l11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ᛻")] = response.status_code
        return bstack11ll1111lll_opy_
    @staticmethod
    def bstack11ll111lll1_opy_(bstack11ll111ll1l_opy_):
        bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡕࡨࡲࡩࡹࠠࡢࠢࡊࡉ࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣ࡫ࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᛼")
        bstack11ll11l1111_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ᛽"), bstack11l1l11_opy_ (u"࠭ࠧ᛾"))
        headers = {
            bstack11l1l11_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧ᛿"): bstack11l1l11_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᜀ").format(bstack11ll11l1111_opy_),
            bstack11l1l11_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᜁ"): bstack11l1l11_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᜂ")
        }
        response = requests.get(bstack11ll111ll1l_opy_, headers=headers)
        bstack11ll1111lll_opy_ = {}
        try:
            bstack11ll1111lll_opy_ = response.json()
            logger.debug(bstack11l1l11_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸ࡚ࡺࡩ࡭ࡵ࠽ࠤ࡬࡫ࡴࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᜃ").format(bstack11ll1111lll_opy_))
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᜄ").format(e, response.text))
            pass
        if bstack11ll1111lll_opy_ is not None:
            bstack11ll1111lll_opy_[bstack11l1l11_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᜅ")] = response.headers.get(
                bstack11l1l11_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᜆ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll1111lll_opy_[bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜇ")] = response.status_code
        return bstack11ll1111lll_opy_
    @staticmethod
    def bstack11ll11l11l1_opy_(bstack11ll111l11l_opy_, payload):
        bstack11l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡍࡢ࡭ࡨࡷࠥࡧࠠࡑࡑࡖࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠠࠩࡵࡷࡶ࠮ࡀࠠࡕࡪࡨࠤࡆࡖࡉࠡࡧࡱࡨࡵࡵࡩ࡯ࡶࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡣࡼࡰࡴࡧࡤࠡࠪࡧ࡭ࡨࡺࠩ࠻ࠢࡗ࡬ࡪࠦࡲࡦࡳࡸࡩࡸࡺࠠࡱࡣࡼࡰࡴࡧࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴ࠻ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡁࡑࡋ࠯ࠤࡴࡸࠠࡏࡱࡱࡩࠥ࡯ࡦࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᜈ")
        try:
            url = bstack11l1l11_opy_ (u"ࠥࡿࢂ࠵ࡻࡾࠤᜉ").format(bstack11ll1llll1l_opy_, bstack11ll111l11l_opy_)
            bstack11ll11l1111_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᜊ"), bstack11l1l11_opy_ (u"ࠬ࠭ᜋ"))
            headers = {
                bstack11l1l11_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᜌ"): bstack11l1l11_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᜍ").format(bstack11ll11l1111_opy_),
                bstack11l1l11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᜎ"): bstack11l1l11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᜏ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll111l1ll_opy_ = [200, 202]
            if response.status_code in bstack11ll111l1ll_opy_:
                return response.json()
            else:
                logger.error(bstack11l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤ࠲࡙ࠥࡴࡢࡶࡸࡷ࠿ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᜐ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡹࡴࡠࡥࡲࡰࡱ࡫ࡣࡵࡡࡥࡹ࡮ࡲࡤࡠࡦࡤࡸࡦࡀࠠࡼࡿࠥᜑ").format(e))
            return None