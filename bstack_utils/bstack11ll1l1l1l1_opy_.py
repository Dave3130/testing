# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11lll111111_opy_
logger = logging.getLogger(__name__)
class bstack11ll1ll11ll_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll111l1ll_opy_ = urljoin(builder, bstack1l111ll_opy_ (u"ࠨ࡫ࡶࡷࡺ࡫ࡳࠨᛈ"))
        if params:
            bstack11ll111l1ll_opy_ += bstack1l111ll_opy_ (u"ࠤࡂࡿࢂࠨᛉ").format(urlencode({bstack1l111ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᛊ"): params.get(bstack1l111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᛋ"))}))
        return bstack11ll1ll11ll_opy_.bstack11ll111ll1l_opy_(bstack11ll111l1ll_opy_)
    @staticmethod
    def bstack11ll11l1l1l_opy_(builder,params=None):
        bstack11ll111l1ll_opy_ = urljoin(builder, bstack1l111ll_opy_ (u"ࠬ࡯ࡳࡴࡷࡨࡷ࠲ࡹࡵ࡮࡯ࡤࡶࡾ࠭ᛌ"))
        if params:
            bstack11ll111l1ll_opy_ += bstack1l111ll_opy_ (u"ࠨ࠿ࡼࡿࠥᛍ").format(urlencode({bstack1l111ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᛎ"): params.get(bstack1l111ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᛏ"))}))
        return bstack11ll1ll11ll_opy_.bstack11ll111ll1l_opy_(bstack11ll111l1ll_opy_)
    @staticmethod
    def bstack11ll111ll1l_opy_(bstack11ll111lll1_opy_):
        bstack11ll111l1l1_opy_ = os.environ.get(bstack1l111ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᛐ"), os.environ.get(bstack1l111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᛑ"), bstack1l111ll_opy_ (u"ࠫࠬᛒ")))
        headers = {bstack1l111ll_opy_ (u"ࠬࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᛓ"): bstack1l111ll_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᛔ").format(bstack11ll111l1l1_opy_)}
        response = requests.get(bstack11ll111lll1_opy_, headers=headers)
        bstack11ll11l111l_opy_ = {}
        try:
            bstack11ll11l111l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l111ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᛕ").format(e))
            pass
        if bstack11ll11l111l_opy_ is not None:
            bstack11ll11l111l_opy_[bstack1l111ll_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛖ")] = response.headers.get(bstack1l111ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛗ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11l111l_opy_[bstack1l111ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛘ")] = response.status_code
        return bstack11ll11l111l_opy_
    @staticmethod
    def bstack11ll1l1lll1_opy_(bstack11ll1111lll_opy_, data):
        logger.debug(bstack1l111ll_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡳࡷࠦࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡖࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࠨᛙ"))
        return bstack11ll1ll11ll_opy_.bstack11ll111l111_opy_(bstack1l111ll_opy_ (u"ࠬࡖࡏࡔࡖࠪᛚ"), bstack11ll1111lll_opy_, data=data)
    @staticmethod
    def bstack11ll1ll111l_opy_(bstack11ll1111lll_opy_, data):
        logger.debug(bstack1l111ll_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡖࡪࡷࡵࡦࡵࡷࠤ࡫ࡵࡲࠡࡩࡨࡸ࡙࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡸࠨᛛ"))
        res = bstack11ll1ll11ll_opy_.bstack11ll111l111_opy_(bstack1l111ll_opy_ (u"ࠧࡈࡇࡗࠫᛜ"), bstack11ll1111lll_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll111l111_opy_(method, bstack11ll1111lll_opy_, data=None, params=None, extra_headers=None):
        bstack11ll111l1l1_opy_ = os.environ.get(bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᛝ"), bstack1l111ll_opy_ (u"ࠩࠪᛞ"))
        headers = {
            bstack1l111ll_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᛟ"): bstack1l111ll_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᛠ").format(bstack11ll111l1l1_opy_),
            bstack1l111ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᛡ"): bstack1l111ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᛢ"),
            bstack1l111ll_opy_ (u"ࠧࡂࡥࡦࡩࡵࡺࠧᛣ"): bstack1l111ll_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫᛤ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11lll111111_opy_ + bstack1l111ll_opy_ (u"ࠤ࠲ࠦᛥ") + bstack11ll1111lll_opy_.lstrip(bstack1l111ll_opy_ (u"ࠪ࠳ࠬᛦ"))
        try:
            if method == bstack1l111ll_opy_ (u"ࠫࡌࡋࡔࠨᛧ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1l111ll_opy_ (u"ࠬࡖࡏࡔࡖࠪᛨ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1l111ll_opy_ (u"࠭ࡐࡖࡖࠪᛩ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1l111ll_opy_ (u"ࠢࡖࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥࡎࡔࡕࡒࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࢀࢃࠢᛪ").format(method))
            logger.debug(bstack1l111ll_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡰࡥࡩ࡫ࠠࡵࡱ࡙ࠣࡗࡒ࠺ࠡࡽࢀࠤࡼ࡯ࡴࡩࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࡿࢂࠨ᛫").format(url, method))
            bstack11ll11l111l_opy_ = {}
            try:
                bstack11ll11l111l_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1l111ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠡ࠯ࠣࡿࢂࠨ᛬").format(e, response.text))
            if bstack11ll11l111l_opy_ is not None:
                bstack11ll11l111l_opy_[bstack1l111ll_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫ᛭")] = response.headers.get(
                    bstack1l111ll_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛮ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11l111l_opy_[bstack1l111ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᛯ")] = response.status_code
            return bstack11ll11l111l_opy_
        except Exception as e:
            logger.error(bstack1l111ll_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᛰ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11l11l1_opy_(bstack11ll111lll1_opy_, data):
        bstack1l111ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡘ࡫࡮ࡥࡵࠣࡥࠥࡖࡕࡕࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡺࡨࡦࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᛱ")
        bstack11ll111l1l1_opy_ = os.environ.get(bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᛲ"), bstack1l111ll_opy_ (u"ࠩࠪᛳ"))
        headers = {
            bstack1l111ll_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᛴ"): bstack1l111ll_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᛵ").format(bstack11ll111l1l1_opy_),
            bstack1l111ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᛶ"): bstack1l111ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᛷ")
        }
        response = requests.put(bstack11ll111lll1_opy_, headers=headers, json=data)
        bstack11ll11l111l_opy_ = {}
        try:
            bstack11ll11l111l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l111ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᛸ").format(e))
            pass
        logger.debug(bstack1l111ll_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࡗࡷ࡭ࡱࡹ࠺ࠡࡲࡸࡸࡤ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥ᛹").format(bstack11ll11l111l_opy_))
        if bstack11ll11l111l_opy_ is not None:
            bstack11ll11l111l_opy_[bstack1l111ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪ᛺")] = response.headers.get(
                bstack1l111ll_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫ᛻"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l111l_opy_[bstack1l111ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ᛼")] = response.status_code
        return bstack11ll11l111l_opy_
    @staticmethod
    def bstack11ll11l1111_opy_(bstack11ll111lll1_opy_):
        bstack1l111ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡩࡳࡪࡳࠡࡣࠣࡋࡊ࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡬࡫ࡴࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ᛽")
        bstack11ll111l1l1_opy_ = os.environ.get(bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ᛾"), bstack1l111ll_opy_ (u"ࠧࠨ᛿"))
        headers = {
            bstack1l111ll_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᜀ"): bstack1l111ll_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᜁ").format(bstack11ll111l1l1_opy_),
            bstack1l111ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᜂ"): bstack1l111ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᜃ")
        }
        response = requests.get(bstack11ll111lll1_opy_, headers=headers)
        bstack11ll11l111l_opy_ = {}
        try:
            bstack11ll11l111l_opy_ = response.json()
            logger.debug(bstack1l111ll_opy_ (u"ࠧࡘࡥࡲࡷࡨࡷࡹ࡛ࡴࡪ࡮ࡶ࠾ࠥ࡭ࡥࡵࡡࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᜄ").format(bstack11ll11l111l_opy_))
        except Exception as e:
            logger.debug(bstack1l111ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠥ࠳ࠠࡼࡿࠥᜅ").format(e, response.text))
            pass
        if bstack11ll11l111l_opy_ is not None:
            bstack11ll11l111l_opy_[bstack1l111ll_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᜆ")] = response.headers.get(
                bstack1l111ll_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᜇ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l111l_opy_[bstack1l111ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜈ")] = response.status_code
        return bstack11ll11l111l_opy_
    @staticmethod
    def bstack11ll111llll_opy_(bstack11ll111ll11_opy_, payload):
        bstack1l111ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡎࡣ࡮ࡩࡸࠦࡡࠡࡒࡒࡗ࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴࠡࠪࡶࡸࡷ࠯࠺ࠡࡖ࡫ࡩࠥࡇࡐࡊࠢࡨࡲࡩࡶ࡯ࡪࡰࡷࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡽࡱࡵࡡࡥࠢࠫࡨ࡮ࡩࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡲࡤࡽࡱࡵࡡࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵ࠼ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡂࡒࡌ࠰ࠥࡵࡲࠡࡐࡲࡲࡪࠦࡩࡧࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᜉ")
        try:
            url = bstack1l111ll_opy_ (u"ࠦࢀࢃ࠯ࡼࡿࠥᜊ").format(bstack11lll111111_opy_, bstack11ll111ll11_opy_)
            bstack11ll111l1l1_opy_ = os.environ.get(bstack1l111ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᜋ"), bstack1l111ll_opy_ (u"࠭ࠧᜌ"))
            headers = {
                bstack1l111ll_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᜍ"): bstack1l111ll_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᜎ").format(bstack11ll111l1l1_opy_),
                bstack1l111ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᜏ"): bstack1l111ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᜐ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll111l11l_opy_ = [200, 202]
            if response.status_code in bstack11ll111l11l_opy_:
                return response.json()
            else:
                logger.error(bstack1l111ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥ࠳ࠦࡓࡵࡣࡷࡹࡸࡀࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᜑ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1l111ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡳࡵࡡࡦࡳࡱࡲࡥࡤࡶࡢࡦࡺ࡯࡬ࡥࡡࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᜒ").format(e))
            return None