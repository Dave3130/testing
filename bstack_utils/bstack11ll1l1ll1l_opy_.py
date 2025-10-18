# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1ll1l1l_opy_
logger = logging.getLogger(__name__)
class bstack11ll1l1l11l_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll111l11l_opy_ = urljoin(builder, bstack11l111_opy_ (u"࠭ࡩࡴࡵࡸࡩࡸ࠭ᛍ"))
        if params:
            bstack11ll111l11l_opy_ += bstack11l111_opy_ (u"ࠢࡀࡽࢀࠦᛎ").format(urlencode({bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᛏ"): params.get(bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᛐ"))}))
        return bstack11ll1l1l11l_opy_.bstack11ll111lll1_opy_(bstack11ll111l11l_opy_)
    @staticmethod
    def bstack11ll11l1l1l_opy_(builder,params=None):
        bstack11ll111l11l_opy_ = urljoin(builder, bstack11l111_opy_ (u"ࠪ࡭ࡸࡹࡵࡦࡵ࠰ࡷࡺࡳ࡭ࡢࡴࡼࠫᛑ"))
        if params:
            bstack11ll111l11l_opy_ += bstack11l111_opy_ (u"ࠦࡄࢁࡽࠣᛒ").format(urlencode({bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᛓ"): params.get(bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᛔ"))}))
        return bstack11ll1l1l11l_opy_.bstack11ll111lll1_opy_(bstack11ll111l11l_opy_)
    @staticmethod
    def bstack11ll111lll1_opy_(bstack11ll11l1l11_opy_):
        bstack11ll11l1111_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᛕ"), os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᛖ"), bstack11l111_opy_ (u"ࠩࠪᛗ")))
        headers = {bstack11l111_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᛘ"): bstack11l111_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᛙ").format(bstack11ll11l1111_opy_)}
        response = requests.get(bstack11ll11l1l11_opy_, headers=headers)
        bstack11ll11l11ll_opy_ = {}
        try:
            bstack11ll11l11ll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᛚ").format(e))
            pass
        if bstack11ll11l11ll_opy_ is not None:
            bstack11ll11l11ll_opy_[bstack11l111_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛛ")] = response.headers.get(bstack11l111_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛜ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11l11ll_opy_[bstack11l111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᛝ")] = response.status_code
        return bstack11ll11l11ll_opy_
    @staticmethod
    def bstack11ll1l1l1ll_opy_(bstack11ll111l1l1_opy_, data):
        logger.debug(bstack11l111_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡒࡦࡳࡸࡩࡸࡺࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡔࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࠦᛞ"))
        return bstack11ll1l1l11l_opy_.bstack11ll11l111l_opy_(bstack11l111_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᛟ"), bstack11ll111l1l1_opy_, data=data)
    @staticmethod
    def bstack11ll1llll1l_opy_(bstack11ll111l1l1_opy_, data):
        logger.debug(bstack11l111_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡳࡷࠦࡧࡦࡶࡗࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡶࠦᛠ"))
        res = bstack11ll1l1l11l_opy_.bstack11ll11l111l_opy_(bstack11l111_opy_ (u"ࠬࡍࡅࡕࠩᛡ"), bstack11ll111l1l1_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l111l_opy_(method, bstack11ll111l1l1_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11l1111_opy_ = os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛢ"), bstack11l111_opy_ (u"ࠧࠨᛣ"))
        headers = {
            bstack11l111_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᛤ"): bstack11l111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᛥ").format(bstack11ll11l1111_opy_),
            bstack11l111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᛦ"): bstack11l111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᛧ"),
            bstack11l111_opy_ (u"ࠬࡇࡣࡤࡧࡳࡸࠬᛨ"): bstack11l111_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᛩ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1ll1l1l_opy_ + bstack11l111_opy_ (u"ࠢ࠰ࠤᛪ") + bstack11ll111l1l1_opy_.lstrip(bstack11l111_opy_ (u"ࠨ࠱ࠪ᛫"))
        try:
            if method == bstack11l111_opy_ (u"ࠩࡊࡉ࡙࠭᛬"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack11l111_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ᛭"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack11l111_opy_ (u"ࠫࡕ࡛ࡔࠨᛮ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack11l111_opy_ (u"࡛ࠧ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡌ࡙࡚ࡐࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧᛯ").format(method))
            logger.debug(bstack11l111_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡮ࡣࡧࡩࠥࡺ࡯ࠡࡗࡕࡐ࠿ࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࡽࢀࠦᛰ").format(url, method))
            bstack11ll11l11ll_opy_ = {}
            try:
                bstack11ll11l11ll_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack11l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠦ࠭ࠡࡽࢀࠦᛱ").format(e, response.text))
            if bstack11ll11l11ll_opy_ is not None:
                bstack11ll11l11ll_opy_[bstack11l111_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛲ")] = response.headers.get(
                    bstack11l111_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛳ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11l11ll_opy_[bstack11l111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛴ")] = response.status_code
            return bstack11ll11l11ll_opy_
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶࡧࡶࡸࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠢ࠰ࠤࢀࢃࠢᛵ").format(e, url))
            return None
    @staticmethod
    def bstack11ll111ll1l_opy_(bstack11ll11l1l11_opy_, data):
        bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡩࡳࡪࡳࠡࡣࠣࡔ࡚࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡸ࡭࡫ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᛶ")
        bstack11ll11l1111_opy_ = os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛷ"), bstack11l111_opy_ (u"ࠧࠨᛸ"))
        headers = {
            bstack11l111_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ᛹"): bstack11l111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ᛺").format(bstack11ll11l1111_opy_),
            bstack11l111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ᛻"): bstack11l111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ᛼")
        }
        response = requests.put(bstack11ll11l1l11_opy_, headers=headers, json=data)
        bstack11ll11l11ll_opy_ = {}
        try:
            bstack11ll11l11ll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦ᛽").format(e))
            pass
        logger.debug(bstack11l111_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࡕࡵ࡫࡯ࡷ࠿ࠦࡰࡶࡶࡢࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣ᛾").format(bstack11ll11l11ll_opy_))
        if bstack11ll11l11ll_opy_ is not None:
            bstack11ll11l11ll_opy_[bstack11l111_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨ᛿")] = response.headers.get(
                bstack11l111_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᜀ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l11ll_opy_[bstack11l111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜁ")] = response.status_code
        return bstack11ll11l11ll_opy_
    @staticmethod
    def bstack11ll11l11l1_opy_(bstack11ll11l1l11_opy_):
        bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡧࡱࡨࡸࠦࡡࠡࡉࡈࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡪࡩࡹࠦࡴࡩࡧࠣࡧࡴࡻ࡮ࡵࠢࡲࡪࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᜂ")
        bstack11ll11l1111_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᜃ"), bstack11l111_opy_ (u"ࠬ࠭ᜄ"))
        headers = {
            bstack11l111_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᜅ"): bstack11l111_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᜆ").format(bstack11ll11l1111_opy_),
            bstack11l111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᜇ"): bstack11l111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᜈ")
        }
        response = requests.get(bstack11ll11l1l11_opy_, headers=headers)
        bstack11ll11l11ll_opy_ = {}
        try:
            bstack11ll11l11ll_opy_ = response.json()
            logger.debug(bstack11l111_opy_ (u"ࠥࡖࡪࡷࡵࡦࡵࡷ࡙ࡹ࡯࡬ࡴ࠼ࠣ࡫ࡪࡺ࡟ࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᜉ").format(bstack11ll11l11ll_opy_))
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡊࡔࡑࡑࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᜊ").format(e, response.text))
            pass
        if bstack11ll11l11ll_opy_ is not None:
            bstack11ll11l11ll_opy_[bstack11l111_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᜋ")] = response.headers.get(
                bstack11l111_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᜌ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l11ll_opy_[bstack11l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᜍ")] = response.status_code
        return bstack11ll11l11ll_opy_
    @staticmethod
    def bstack11ll111llll_opy_(bstack11ll111ll11_opy_, payload):
        bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡓࡡ࡬ࡧࡶࠤࡦࠦࡐࡐࡕࡗࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡴࡤࡱࡱ࡬ࡲࡹࠦࠨࡴࡶࡵ࠭࠿ࠦࡔࡩࡧࠣࡅࡕࡏࠠࡦࡰࡧࡴࡴ࡯࡮ࡵࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡢࡻ࡯ࡳࡦࡪࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡸࡥࡲࡷࡨࡷࡹࠦࡰࡢࡻ࡯ࡳࡦࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡇࡐࡊ࠮ࠣࡳࡷࠦࡎࡰࡰࡨࠤ࡮࡬ࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᜎ")
        try:
            url = bstack11l111_opy_ (u"ࠤࡾࢁ࠴ࢁࡽࠣᜏ").format(bstack11ll1ll1l1l_opy_, bstack11ll111ll11_opy_)
            bstack11ll11l1111_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᜐ"), bstack11l111_opy_ (u"ࠫࠬᜑ"))
            headers = {
                bstack11l111_opy_ (u"ࠬࡧࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᜒ"): bstack11l111_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᜓ").format(bstack11ll11l1111_opy_),
                bstack11l111_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ᜔࠭"): bstack11l111_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱ᜕ࠫ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll111l1ll_opy_ = [200, 202]
            if response.status_code in bstack11ll111l1ll_opy_:
                return response.json()
            else:
                logger.error(bstack11l111_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣ࠱ࠤࡘࡺࡡࡵࡷࡶ࠾ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣ᜖").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡸࡺ࡟ࡤࡱ࡯ࡰࡪࡩࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡻࡾࠤ᜗").format(e))
            return None