# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1l1lll1_opy_
logger = logging.getLogger(__name__)
class bstack11ll1l1l1l1_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll1111lll_opy_ = urljoin(builder, bstack11l1111_opy_ (u"࠭ࡩࡴࡵࡸࡩࡸ࠭ᛩ"))
        if params:
            bstack11ll1111lll_opy_ += bstack11l1111_opy_ (u"ࠢࡀࡽࢀࠦᛪ").format(urlencode({bstack11l1111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᛫"): params.get(bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᛬"))}))
        return bstack11ll1l1l1l1_opy_.bstack11ll1111l11_opy_(bstack11ll1111lll_opy_)
    @staticmethod
    def bstack11ll111lll1_opy_(builder,params=None):
        bstack11ll1111lll_opy_ = urljoin(builder, bstack11l1111_opy_ (u"ࠪ࡭ࡸࡹࡵࡦࡵ࠰ࡷࡺࡳ࡭ࡢࡴࡼࠫ᛭"))
        if params:
            bstack11ll1111lll_opy_ += bstack11l1111_opy_ (u"ࠦࡄࢁࡽࠣᛮ").format(urlencode({bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᛯ"): params.get(bstack11l1111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᛰ"))}))
        return bstack11ll1l1l1l1_opy_.bstack11ll1111l11_opy_(bstack11ll1111lll_opy_)
    @staticmethod
    def bstack11ll1111l11_opy_(bstack11ll11111l1_opy_):
        bstack11ll1111l1l_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᛱ"), os.environ.get(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᛲ"), bstack11l1111_opy_ (u"ࠩࠪᛳ")))
        headers = {bstack11l1111_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᛴ"): bstack11l1111_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᛵ").format(bstack11ll1111l1l_opy_)}
        response = requests.get(bstack11ll11111l1_opy_, headers=headers)
        bstack11ll111l11l_opy_ = {}
        try:
            bstack11ll111l11l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᛶ").format(e))
            pass
        if bstack11ll111l11l_opy_ is not None:
            bstack11ll111l11l_opy_[bstack11l1111_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛷ")] = response.headers.get(bstack11l1111_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛸ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll111l11l_opy_[bstack11l1111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ᛹")] = response.status_code
        return bstack11ll111l11l_opy_
    @staticmethod
    def bstack11ll1ll1l11_opy_(bstack11ll1111111_opy_, data):
        logger.debug(bstack11l1111_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡒࡦࡳࡸࡩࡸࡺࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡔࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࠦ᛺"))
        return bstack11ll1l1l1l1_opy_.bstack11ll111l1l1_opy_(bstack11l1111_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ᛻"), bstack11ll1111111_opy_, data=data)
    @staticmethod
    def bstack11ll1l111l1_opy_(bstack11ll1111111_opy_, data):
        logger.debug(bstack11l1111_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡳࡷࠦࡧࡦࡶࡗࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡶࠦ᛼"))
        res = bstack11ll1l1l1l1_opy_.bstack11ll111l1l1_opy_(bstack11l1111_opy_ (u"ࠬࡍࡅࡕࠩ᛽"), bstack11ll1111111_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll111l1l1_opy_(method, bstack11ll1111111_opy_, data=None, params=None, extra_headers=None):
        bstack11ll1111l1l_opy_ = os.environ.get(bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ᛾"), bstack11l1111_opy_ (u"ࠧࠨ᛿"))
        headers = {
            bstack11l1111_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᜀ"): bstack11l1111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᜁ").format(bstack11ll1111l1l_opy_),
            bstack11l1111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᜂ"): bstack11l1111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᜃ"),
            bstack11l1111_opy_ (u"ࠬࡇࡣࡤࡧࡳࡸࠬᜄ"): bstack11l1111_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᜅ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1l1lll1_opy_ + bstack11l1111_opy_ (u"ࠢ࠰ࠤᜆ") + bstack11ll1111111_opy_.lstrip(bstack11l1111_opy_ (u"ࠨ࠱ࠪᜇ"))
        try:
            if method == bstack11l1111_opy_ (u"ࠩࡊࡉ࡙࠭ᜈ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack11l1111_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᜉ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack11l1111_opy_ (u"ࠫࡕ࡛ࡔࠨᜊ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack11l1111_opy_ (u"࡛ࠧ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡌ࡙࡚ࡐࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧᜋ").format(method))
            logger.debug(bstack11l1111_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡮ࡣࡧࡩࠥࡺ࡯ࠡࡗࡕࡐ࠿ࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࡽࢀࠦᜌ").format(url, method))
            bstack11ll111l11l_opy_ = {}
            try:
                bstack11ll111l11l_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack11l1111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠦ࠭ࠡࡽࢀࠦᜍ").format(e, response.text))
            if bstack11ll111l11l_opy_ is not None:
                bstack11ll111l11l_opy_[bstack11l1111_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᜎ")] = response.headers.get(
                    bstack11l1111_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᜏ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll111l11l_opy_[bstack11l1111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᜐ")] = response.status_code
            return bstack11ll111l11l_opy_
        except Exception as e:
            logger.error(bstack11l1111_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶࡧࡶࡸࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠢ࠰ࠤࢀࢃࠢᜑ").format(e, url))
            return None
    @staticmethod
    def bstack11ll111111l_opy_(bstack11ll11111l1_opy_, data):
        bstack11l1111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡩࡳࡪࡳࠡࡣࠣࡔ࡚࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡸ࡭࡫ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᜒ")
        bstack11ll1111l1l_opy_ = os.environ.get(bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᜓ"), bstack11l1111_opy_ (u"ࠧࠨ᜔"))
        headers = {
            bstack11l1111_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ᜕"): bstack11l1111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ᜖").format(bstack11ll1111l1l_opy_),
            bstack11l1111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ᜗"): bstack11l1111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ᜘")
        }
        response = requests.put(bstack11ll11111l1_opy_, headers=headers, json=data)
        bstack11ll111l11l_opy_ = {}
        try:
            bstack11ll111l11l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦ᜙").format(e))
            pass
        logger.debug(bstack11l1111_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࡕࡵ࡫࡯ࡷ࠿ࠦࡰࡶࡶࡢࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣ᜚").format(bstack11ll111l11l_opy_))
        if bstack11ll111l11l_opy_ is not None:
            bstack11ll111l11l_opy_[bstack11l1111_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨ᜛")] = response.headers.get(
                bstack11l1111_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩ᜜"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll111l11l_opy_[bstack11l1111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ᜝")] = response.status_code
        return bstack11ll111l11l_opy_
    @staticmethod
    def bstack11ll111l1ll_opy_(bstack11ll11111l1_opy_):
        bstack11l1111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡧࡱࡨࡸࠦࡡࠡࡉࡈࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡪࡩࡹࠦࡴࡩࡧࠣࡧࡴࡻ࡮ࡵࠢࡲࡪࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ᜞")
        bstack11ll1111l1l_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᜟ"), bstack11l1111_opy_ (u"ࠬ࠭ᜠ"))
        headers = {
            bstack11l1111_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᜡ"): bstack11l1111_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᜢ").format(bstack11ll1111l1l_opy_),
            bstack11l1111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᜣ"): bstack11l1111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᜤ")
        }
        response = requests.get(bstack11ll11111l1_opy_, headers=headers)
        bstack11ll111l11l_opy_ = {}
        try:
            bstack11ll111l11l_opy_ = response.json()
            logger.debug(bstack11l1111_opy_ (u"ࠥࡖࡪࡷࡵࡦࡵࡷ࡙ࡹ࡯࡬ࡴ࠼ࠣ࡫ࡪࡺ࡟ࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᜥ").format(bstack11ll111l11l_opy_))
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡊࡔࡑࡑࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᜦ").format(e, response.text))
            pass
        if bstack11ll111l11l_opy_ is not None:
            bstack11ll111l11l_opy_[bstack11l1111_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᜧ")] = response.headers.get(
                bstack11l1111_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᜨ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll111l11l_opy_[bstack11l1111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᜩ")] = response.status_code
        return bstack11ll111l11l_opy_
    @staticmethod
    def bstack11ll1111ll1_opy_(bstack11ll111l111_opy_, payload):
        bstack11l1111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡓࡡ࡬ࡧࡶࠤࡦࠦࡐࡐࡕࡗࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡴࡤࡱࡱ࡬ࡲࡹࠦࠨࡴࡶࡵ࠭࠿ࠦࡔࡩࡧࠣࡅࡕࡏࠠࡦࡰࡧࡴࡴ࡯࡮ࡵࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡢࡻ࡯ࡳࡦࡪࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡸࡥࡲࡷࡨࡷࡹࠦࡰࡢࡻ࡯ࡳࡦࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡇࡐࡊ࠮ࠣࡳࡷࠦࡎࡰࡰࡨࠤ࡮࡬ࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᜪ")
        try:
            url = bstack11l1111_opy_ (u"ࠤࡾࢁ࠴ࢁࡽࠣᜫ").format(bstack11ll1l1lll1_opy_, bstack11ll111l111_opy_)
            bstack11ll1111l1l_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᜬ"), bstack11l1111_opy_ (u"ࠫࠬᜭ"))
            headers = {
                bstack11l1111_opy_ (u"ࠬࡧࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᜮ"): bstack11l1111_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᜯ").format(bstack11ll1111l1l_opy_),
                bstack11l1111_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ᜰ"): bstack11l1111_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫᜱ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11111ll_opy_ = [200, 202]
            if response.status_code in bstack11ll11111ll_opy_:
                return response.json()
            else:
                logger.error(bstack11l1111_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣ࠱ࠤࡘࡺࡡࡵࡷࡶ࠾ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᜲ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack11l1111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡸࡺ࡟ࡤࡱ࡯ࡰࡪࡩࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᜳ").format(e))
            return None