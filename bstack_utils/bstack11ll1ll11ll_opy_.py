# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1l1llll_opy_
logger = logging.getLogger(__name__)
class bstack11ll1l111l1_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll1111111_opy_ = urljoin(builder, bstack11ll1ll_opy_ (u"ࠧࡪࡵࡶࡹࡪࡹࠧᛪ"))
        if params:
            bstack11ll1111111_opy_ += bstack11ll1ll_opy_ (u"ࠣࡁࡾࢁࠧ᛫").format(urlencode({bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᛬"): params.get(bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᛭"))}))
        return bstack11ll1l111l1_opy_.bstack11ll1111l11_opy_(bstack11ll1111111_opy_)
    @staticmethod
    def bstack11ll111llll_opy_(builder,params=None):
        bstack11ll1111111_opy_ = urljoin(builder, bstack11ll1ll_opy_ (u"ࠫ࡮ࡹࡳࡶࡧࡶ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠬᛮ"))
        if params:
            bstack11ll1111111_opy_ += bstack11ll1ll_opy_ (u"ࠧࡅࡻࡾࠤᛯ").format(urlencode({bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᛰ"): params.get(bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᛱ"))}))
        return bstack11ll1l111l1_opy_.bstack11ll1111l11_opy_(bstack11ll1111111_opy_)
    @staticmethod
    def bstack11ll1111l11_opy_(bstack11ll111l1l1_opy_):
        bstack11ll111l1ll_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᛲ"), os.environ.get(bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᛳ"), bstack11ll1ll_opy_ (u"ࠪࠫᛴ")))
        headers = {bstack11ll1ll_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᛵ"): bstack11ll1ll_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᛶ").format(bstack11ll111l1ll_opy_)}
        response = requests.get(bstack11ll111l1l1_opy_, headers=headers)
        bstack11ll1111lll_opy_ = {}
        try:
            bstack11ll1111lll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛷ").format(e))
            pass
        if bstack11ll1111lll_opy_ is not None:
            bstack11ll1111lll_opy_[bstack11ll1ll_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛸ")] = response.headers.get(bstack11ll1ll_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩ᛹"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll1111lll_opy_[bstack11ll1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ᛺")] = response.status_code
        return bstack11ll1111lll_opy_
    @staticmethod
    def bstack11ll1ll1ll1_opy_(bstack11ll111111l_opy_, data):
        logger.debug(bstack11ll1ll_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡓࡧࡴࡹࡪࡹࡴࠡࡨࡲࡶࠥࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࠧ᛻"))
        return bstack11ll1l111l1_opy_.bstack11ll1111l1l_opy_(bstack11ll1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩ᛼"), bstack11ll111111l_opy_, data=data)
    @staticmethod
    def bstack11ll1ll111l_opy_(bstack11ll111111l_opy_, data):
        logger.debug(bstack11ll1ll_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡕࡩࡶࡻࡥࡴࡶࠣࡪࡴࡸࠠࡨࡧࡷࡘࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡷࠧ᛽"))
        res = bstack11ll1l111l1_opy_.bstack11ll1111l1l_opy_(bstack11ll1ll_opy_ (u"࠭ࡇࡆࡖࠪ᛾"), bstack11ll111111l_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll1111l1l_opy_(method, bstack11ll111111l_opy_, data=None, params=None, extra_headers=None):
        bstack11ll111l1ll_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ᛿"), bstack11ll1ll_opy_ (u"ࠨࠩᜀ"))
        headers = {
            bstack11ll1ll_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᜁ"): bstack11ll1ll_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᜂ").format(bstack11ll111l1ll_opy_),
            bstack11ll1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᜃ"): bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᜄ"),
            bstack11ll1ll_opy_ (u"࠭ࡁࡤࡥࡨࡴࡹ࠭ᜅ"): bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᜆ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1l1llll_opy_ + bstack11ll1ll_opy_ (u"ࠣ࠱ࠥᜇ") + bstack11ll111111l_opy_.lstrip(bstack11ll1ll_opy_ (u"ࠩ࠲ࠫᜈ"))
        try:
            if method == bstack11ll1ll_opy_ (u"ࠪࡋࡊ࡚ࠧᜉ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack11ll1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩᜊ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack11ll1ll_opy_ (u"ࠬࡖࡕࡕࠩᜋ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack11ll1ll_opy_ (u"ࠨࡕ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡍ࡚ࡔࡑࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࡿࢂࠨᜌ").format(method))
            logger.debug(bstack11ll1ll_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹࡪࡹࡴࠡ࡯ࡤࡨࡪࠦࡴࡰࠢࡘࡖࡑࡀࠠࡼࡿࠣࡻ࡮ࡺࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧᜍ").format(url, method))
            bstack11ll1111lll_opy_ = {}
            try:
                bstack11ll1111lll_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack11ll1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧᜎ").format(e, response.text))
            if bstack11ll1111lll_opy_ is not None:
                bstack11ll1111lll_opy_[bstack11ll1ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᜏ")] = response.headers.get(
                    bstack11ll1ll_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᜐ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll1111lll_opy_[bstack11ll1ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᜑ")] = response.status_code
            return bstack11ll1111lll_opy_
        except Exception as e:
            logger.error(bstack11ll1ll_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᜒ").format(e, url))
            return None
    @staticmethod
    def bstack11ll111l11l_opy_(bstack11ll111l1l1_opy_, data):
        bstack11ll1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡪࡴࡤࡴࠢࡤࠤࡕ࡛ࡔࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᜓ")
        bstack11ll111l1ll_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗ᜔ࠫ"), bstack11ll1ll_opy_ (u"ࠨ᜕ࠩ"))
        headers = {
            bstack11ll1ll_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ᜖"): bstack11ll1ll_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭᜗").format(bstack11ll111l1ll_opy_),
            bstack11ll1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ᜘"): bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ᜙")
        }
        response = requests.put(bstack11ll111l1l1_opy_, headers=headers, json=data)
        bstack11ll1111lll_opy_ = {}
        try:
            bstack11ll1111lll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧ᜚").format(e))
            pass
        logger.debug(bstack11ll1ll_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࡖࡶ࡬ࡰࡸࡀࠠࡱࡷࡷࡣ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤ᜛").format(bstack11ll1111lll_opy_))
        if bstack11ll1111lll_opy_ is not None:
            bstack11ll1111lll_opy_[bstack11ll1ll_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩ᜜")] = response.headers.get(
                bstack11ll1ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪ᜝"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll1111lll_opy_[bstack11ll1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ᜞")] = response.status_code
        return bstack11ll1111lll_opy_
    @staticmethod
    def bstack11ll1111ll1_opy_(bstack11ll111l1l1_opy_):
        bstack11ll1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡕࡨࡲࡩࡹࠠࡢࠢࡊࡉ࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣ࡫ࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᜟ")
        bstack11ll111l1ll_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᜠ"), bstack11ll1ll_opy_ (u"࠭ࠧᜡ"))
        headers = {
            bstack11ll1ll_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᜢ"): bstack11ll1ll_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᜣ").format(bstack11ll111l1ll_opy_),
            bstack11ll1ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᜤ"): bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᜥ")
        }
        response = requests.get(bstack11ll111l1l1_opy_, headers=headers)
        bstack11ll1111lll_opy_ = {}
        try:
            bstack11ll1111lll_opy_ = response.json()
            logger.debug(bstack11ll1ll_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸ࡚ࡺࡩ࡭ࡵ࠽ࠤ࡬࡫ࡴࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᜦ").format(bstack11ll1111lll_opy_))
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᜧ").format(e, response.text))
            pass
        if bstack11ll1111lll_opy_ is not None:
            bstack11ll1111lll_opy_[bstack11ll1ll_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᜨ")] = response.headers.get(
                bstack11ll1ll_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᜩ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll1111lll_opy_[bstack11ll1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜪ")] = response.status_code
        return bstack11ll1111lll_opy_
    @staticmethod
    def bstack11ll11111l1_opy_(bstack11ll11111ll_opy_, payload):
        bstack11ll1ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡍࡢ࡭ࡨࡷࠥࡧࠠࡑࡑࡖࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠠࠩࡵࡷࡶ࠮ࡀࠠࡕࡪࡨࠤࡆࡖࡉࠡࡧࡱࡨࡵࡵࡩ࡯ࡶࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡣࡼࡰࡴࡧࡤࠡࠪࡧ࡭ࡨࡺࠩ࠻ࠢࡗ࡬ࡪࠦࡲࡦࡳࡸࡩࡸࡺࠠࡱࡣࡼࡰࡴࡧࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴ࠻ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡁࡑࡋ࠯ࠤࡴࡸࠠࡏࡱࡱࡩࠥ࡯ࡦࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᜫ")
        try:
            url = bstack11ll1ll_opy_ (u"ࠥࡿࢂ࠵ࡻࡾࠤᜬ").format(bstack11ll1l1llll_opy_, bstack11ll11111ll_opy_)
            bstack11ll111l1ll_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᜭ"), bstack11ll1ll_opy_ (u"ࠬ࠭ᜮ"))
            headers = {
                bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᜯ"): bstack11ll1ll_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᜰ").format(bstack11ll111l1ll_opy_),
                bstack11ll1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᜱ"): bstack11ll1ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᜲ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll111l111_opy_ = [200, 202]
            if response.status_code in bstack11ll111l111_opy_:
                return response.json()
            else:
                logger.error(bstack11ll1ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤ࠲࡙ࠥࡴࡢࡶࡸࡷ࠿ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᜳ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack11ll1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡹࡴࡠࡥࡲࡰࡱ࡫ࡣࡵࡡࡥࡹ࡮ࡲࡤࡠࡦࡤࡸࡦࡀࠠࡼࡿ᜴ࠥ").format(e))
            return None