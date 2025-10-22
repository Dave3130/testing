# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1lll11l_opy_
logger = logging.getLogger(__name__)
class bstack11ll1l1llll_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11l11ll_opy_ = urljoin(builder, bstack1lllll1l_opy_ (u"ࠫ࡮ࡹࡳࡶࡧࡶࠫᛋ"))
        if params:
            bstack11ll11l11ll_opy_ += bstack1lllll1l_opy_ (u"ࠧࡅࡻࡾࠤᛌ").format(urlencode({bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᛍ"): params.get(bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᛎ"))}))
        return bstack11ll1l1llll_opy_.bstack11ll111l1l1_opy_(bstack11ll11l11ll_opy_)
    @staticmethod
    def bstack11ll11ll111_opy_(builder,params=None):
        bstack11ll11l11ll_opy_ = urljoin(builder, bstack1lllll1l_opy_ (u"ࠨ࡫ࡶࡷࡺ࡫ࡳ࠮ࡵࡸࡱࡲࡧࡲࡺࠩᛏ"))
        if params:
            bstack11ll11l11ll_opy_ += bstack1lllll1l_opy_ (u"ࠤࡂࡿࢂࠨᛐ").format(urlencode({bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᛑ"): params.get(bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᛒ"))}))
        return bstack11ll1l1llll_opy_.bstack11ll111l1l1_opy_(bstack11ll11l11ll_opy_)
    @staticmethod
    def bstack11ll111l1l1_opy_(bstack11ll11l111l_opy_):
        bstack11ll111llll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᛓ"), os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛔ"), bstack1lllll1l_opy_ (u"ࠧࠨᛕ")))
        headers = {bstack1lllll1l_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᛖ"): bstack1lllll1l_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᛗ").format(bstack11ll111llll_opy_)}
        response = requests.get(bstack11ll11l111l_opy_, headers=headers)
        bstack11ll11l1l11_opy_ = {}
        try:
            bstack11ll11l1l11_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᛘ").format(e))
            pass
        if bstack11ll11l1l11_opy_ is not None:
            bstack11ll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛙ")] = response.headers.get(bstack1lllll1l_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛚ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11l1l11_opy_[bstack1lllll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᛛ")] = response.status_code
        return bstack11ll11l1l11_opy_
    @staticmethod
    def bstack11ll1ll1l1l_opy_(bstack11ll111l1ll_opy_, data):
        logger.debug(bstack1lllll1l_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡗ࡫ࡱࡶࡧࡶࡸࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࡙ࡰ࡭࡫ࡷࡘࡪࡹࡴࡴࠤᛜ"))
        return bstack11ll1l1llll_opy_.bstack11ll111lll1_opy_(bstack1lllll1l_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᛝ"), bstack11ll111l1ll_opy_, data=data)
    @staticmethod
    def bstack11ll1llllll_opy_(bstack11ll111l1ll_opy_, data):
        logger.debug(bstack1lllll1l_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡒࡦࡳࡸࡩࡸࡺࠠࡧࡱࡵࠤ࡬࡫ࡴࡕࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡴࠤᛞ"))
        res = bstack11ll1l1llll_opy_.bstack11ll111lll1_opy_(bstack1lllll1l_opy_ (u"ࠪࡋࡊ࡚ࠧᛟ"), bstack11ll111l1ll_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll111lll1_opy_(method, bstack11ll111l1ll_opy_, data=None, params=None, extra_headers=None):
        bstack11ll111llll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᛠ"), bstack1lllll1l_opy_ (u"ࠬ࠭ᛡ"))
        headers = {
            bstack1lllll1l_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᛢ"): bstack1lllll1l_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᛣ").format(bstack11ll111llll_opy_),
            bstack1lllll1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᛤ"): bstack1lllll1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᛥ"),
            bstack1lllll1l_opy_ (u"ࠪࡅࡨࡩࡥࡱࡶࠪᛦ"): bstack1lllll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᛧ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1lll11l_opy_ + bstack1lllll1l_opy_ (u"ࠧ࠵ࠢᛨ") + bstack11ll111l1ll_opy_.lstrip(bstack1lllll1l_opy_ (u"࠭࠯ࠨᛩ"))
        try:
            if method == bstack1lllll1l_opy_ (u"ࠧࡈࡇࡗࠫᛪ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1lllll1l_opy_ (u"ࠨࡒࡒࡗ࡙࠭᛫"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1lllll1l_opy_ (u"ࠩࡓ࡙࡙࠭᛬"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1lllll1l_opy_ (u"࡙ࠥࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡊࡗࡘࡕࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࡼࡿࠥ᛭").format(method))
            logger.debug(bstack1lllll1l_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡳࡡࡥࡧࠣࡸࡴࠦࡕࡓࡎ࠽ࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡳࡥࡵࡪࡲࡨ࠿ࠦࡻࡾࠤᛮ").format(url, method))
            bstack11ll11l1l11_opy_ = {}
            try:
                bstack11ll11l1l11_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1lllll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᛯ").format(e, response.text))
            if bstack11ll11l1l11_opy_ is not None:
                bstack11ll11l1l11_opy_[bstack1lllll1l_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛰ")] = response.headers.get(
                    bstack1lllll1l_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛱ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᛲ")] = response.status_code
            return bstack11ll11l1l11_opy_
        except Exception as e:
            logger.error(bstack1lllll1l_opy_ (u"ࠤࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡵࡩࡶࡻࡥࡴࡶࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧᛳ").format(e, url))
            return None
    @staticmethod
    def bstack11ll111l11l_opy_(bstack11ll11l111l_opy_, data):
        bstack1lllll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡧࡱࡨࡸࠦࡡࠡࡒࡘࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡶ࡫ࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᛴ")
        bstack11ll111llll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᛵ"), bstack1lllll1l_opy_ (u"ࠬ࠭ᛶ"))
        headers = {
            bstack1lllll1l_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᛷ"): bstack1lllll1l_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᛸ").format(bstack11ll111llll_opy_),
            bstack1lllll1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ᛹"): bstack1lllll1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ᛺")
        }
        response = requests.put(bstack11ll11l111l_opy_, headers=headers, json=data)
        bstack11ll11l1l11_opy_ = {}
        try:
            bstack11ll11l1l11_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤ᛻").format(e))
            pass
        logger.debug(bstack1lllll1l_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸ࡚ࡺࡩ࡭ࡵ࠽ࠤࡵࡻࡴࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨ᛼").format(bstack11ll11l1l11_opy_))
        if bstack11ll11l1l11_opy_ is not None:
            bstack11ll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭᛽")] = response.headers.get(
                bstack1lllll1l_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧ᛾"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ᛿")] = response.status_code
        return bstack11ll11l1l11_opy_
    @staticmethod
    def bstack11ll111ll11_opy_(bstack11ll11l111l_opy_):
        bstack1lllll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡥ࡯ࡦࡶࠤࡦࠦࡇࡆࡖࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡨࡧࡷࠤࡹ࡮ࡥࠡࡥࡲࡹࡳࡺࠠࡰࡨࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᜀ")
        bstack11ll111llll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᜁ"), bstack1lllll1l_opy_ (u"ࠪࠫᜂ"))
        headers = {
            bstack1lllll1l_opy_ (u"ࠫࡦࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᜃ"): bstack1lllll1l_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᜄ").format(bstack11ll111llll_opy_),
            bstack1lllll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᜅ"): bstack1lllll1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᜆ")
        }
        response = requests.get(bstack11ll11l111l_opy_, headers=headers)
        bstack11ll11l1l11_opy_ = {}
        try:
            bstack11ll11l1l11_opy_ = response.json()
            logger.debug(bstack1lllll1l_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࡗࡷ࡭ࡱࡹ࠺ࠡࡩࡨࡸࡤ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᜇ").format(bstack11ll11l1l11_opy_))
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠡ࠯ࠣࡿࢂࠨᜈ").format(e, response.text))
            pass
        if bstack11ll11l1l11_opy_ is not None:
            bstack11ll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᜉ")] = response.headers.get(
                bstack1lllll1l_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᜊ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᜋ")] = response.status_code
        return bstack11ll11l1l11_opy_
    @staticmethod
    def bstack11ll111ll1l_opy_(bstack11ll11l1111_opy_, payload):
        bstack1lllll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡑࡦࡱࡥࡴࠢࡤࠤࡕࡕࡓࡕࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡴࡩࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠡࡧࡱࡨࡵࡵࡩ࡯ࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡲࡩࡶ࡯ࡪࡰࡷࠤ࠭ࡹࡴࡳࠫ࠽ࠤ࡙࡮ࡥࠡࡃࡓࡍࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡹ࡭ࡱࡤࡨࠥ࠮ࡤࡪࡥࡷ࠭࠿ࠦࡔࡩࡧࠣࡶࡪࡷࡵࡦࡵࡷࠤࡵࡧࡹ࡭ࡱࡤࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡅࡕࡏࠬࠡࡱࡵࠤࡓࡵ࡮ࡦࠢ࡬ࡪࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᜌ")
        try:
            url = bstack1lllll1l_opy_ (u"ࠢࡼࡿ࠲ࡿࢂࠨᜍ").format(bstack11ll1lll11l_opy_, bstack11ll11l1111_opy_)
            bstack11ll111llll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᜎ"), bstack1lllll1l_opy_ (u"ࠩࠪᜏ"))
            headers = {
                bstack1lllll1l_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᜐ"): bstack1lllll1l_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᜑ").format(bstack11ll111llll_opy_),
                bstack1lllll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᜒ"): bstack1lllll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᜓ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11l11l1_opy_ = [200, 202]
            if response.status_code in bstack11ll11l11l1_opy_:
                return response.json()
            else:
                logger.error(bstack1lllll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡲ࡬ࡦࡥࡷࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡ࠯ࠢࡖࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨ᜔").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡶࡸࡤࡩ࡯࡭࡮ࡨࡧࡹࡥࡢࡶ࡫࡯ࡨࡤࡪࡡࡵࡣ࠽ࠤࢀࢃ᜕ࠢ").format(e))
            return None