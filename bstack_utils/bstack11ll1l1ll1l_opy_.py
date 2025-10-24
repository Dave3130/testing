# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1ll1111_opy_
logger = logging.getLogger(__name__)
class bstack11ll1lll1ll_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll111l1ll_opy_ = urljoin(builder, bstack1l1_opy_ (u"ࠧࡪࡵࡶࡹࡪࡹࠧᛀ"))
        if params:
            bstack11ll111l1ll_opy_ += bstack1l1_opy_ (u"ࠣࡁࡾࢁࠧᛁ").format(urlencode({bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᛂ"): params.get(bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᛃ"))}))
        return bstack11ll1lll1ll_opy_.bstack11ll111ll1l_opy_(bstack11ll111l1ll_opy_)
    @staticmethod
    def bstack11ll11ll111_opy_(builder,params=None):
        bstack11ll111l1ll_opy_ = urljoin(builder, bstack1l1_opy_ (u"ࠫ࡮ࡹࡳࡶࡧࡶ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠬᛄ"))
        if params:
            bstack11ll111l1ll_opy_ += bstack1l1_opy_ (u"ࠧࡅࡻࡾࠤᛅ").format(urlencode({bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᛆ"): params.get(bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᛇ"))}))
        return bstack11ll1lll1ll_opy_.bstack11ll111ll1l_opy_(bstack11ll111l1ll_opy_)
    @staticmethod
    def bstack11ll111ll1l_opy_(bstack11ll11l1ll1_opy_):
        bstack11ll11l1l11_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᛈ"), os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᛉ"), bstack1l1_opy_ (u"ࠪࠫᛊ")))
        headers = {bstack1l1_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᛋ"): bstack1l1_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᛌ").format(bstack11ll11l1l11_opy_)}
        response = requests.get(bstack11ll11l1ll1_opy_, headers=headers)
        bstack11ll111lll1_opy_ = {}
        try:
            bstack11ll111lll1_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛍ").format(e))
            pass
        if bstack11ll111lll1_opy_ is not None:
            bstack11ll111lll1_opy_[bstack1l1_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛎ")] = response.headers.get(bstack1l1_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛏ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll111lll1_opy_[bstack1l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛐ")] = response.status_code
        return bstack11ll111lll1_opy_
    @staticmethod
    def bstack11ll1lll11l_opy_(bstack11ll11l111l_opy_, data):
        logger.debug(bstack1l1_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡓࡧࡴࡹࡪࡹࡴࠡࡨࡲࡶࠥࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࠧᛑ"))
        return bstack11ll1lll1ll_opy_.bstack11ll11l1111_opy_(bstack1l1_opy_ (u"ࠫࡕࡕࡓࡕࠩᛒ"), bstack11ll11l111l_opy_, data=data)
    @staticmethod
    def bstack11lll11111l_opy_(bstack11ll11l111l_opy_, data):
        logger.debug(bstack1l1_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡕࡩࡶࡻࡥࡴࡶࠣࡪࡴࡸࠠࡨࡧࡷࡘࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡷࠧᛓ"))
        res = bstack11ll1lll1ll_opy_.bstack11ll11l1111_opy_(bstack1l1_opy_ (u"࠭ࡇࡆࡖࠪᛔ"), bstack11ll11l111l_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l1111_opy_(method, bstack11ll11l111l_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11l1l11_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛕ"), bstack1l1_opy_ (u"ࠨࠩᛖ"))
        headers = {
            bstack1l1_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛗ"): bstack1l1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛘ").format(bstack11ll11l1l11_opy_),
            bstack1l1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛙ"): bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛚ"),
            bstack1l1_opy_ (u"࠭ࡁࡤࡥࡨࡴࡹ࠭ᛛ"): bstack1l1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᛜ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1ll1111_opy_ + bstack1l1_opy_ (u"ࠣ࠱ࠥᛝ") + bstack11ll11l111l_opy_.lstrip(bstack1l1_opy_ (u"ࠩ࠲ࠫᛞ"))
        try:
            if method == bstack1l1_opy_ (u"ࠪࡋࡊ࡚ࠧᛟ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1l1_opy_ (u"ࠫࡕࡕࡓࡕࠩᛠ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1l1_opy_ (u"ࠬࡖࡕࡕࠩᛡ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1l1_opy_ (u"ࠨࡕ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡍ࡚ࡔࡑࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࡿࢂࠨᛢ").format(method))
            logger.debug(bstack1l1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹࡪࡹࡴࠡ࡯ࡤࡨࡪࠦࡴࡰࠢࡘࡖࡑࡀࠠࡼࡿࠣࡻ࡮ࡺࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧᛣ").format(url, method))
            bstack11ll111lll1_opy_ = {}
            try:
                bstack11ll111lll1_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧᛤ").format(e, response.text))
            if bstack11ll111lll1_opy_ is not None:
                bstack11ll111lll1_opy_[bstack1l1_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛥ")] = response.headers.get(
                    bstack1l1_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛦ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll111lll1_opy_[bstack1l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᛧ")] = response.status_code
            return bstack11ll111lll1_opy_
        except Exception as e:
            logger.error(bstack1l1_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᛨ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11l1l1l_opy_(bstack11ll11l1ll1_opy_, data):
        bstack1l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡪࡴࡤࡴࠢࡤࠤࡕ࡛ࡔࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᛩ")
        bstack11ll11l1l11_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛪ"), bstack1l1_opy_ (u"ࠨࠩ᛫"))
        headers = {
            bstack1l1_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ᛬"): bstack1l1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭᛭").format(bstack11ll11l1l11_opy_),
            bstack1l1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛮ"): bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛯ")
        }
        response = requests.put(bstack11ll11l1ll1_opy_, headers=headers, json=data)
        bstack11ll111lll1_opy_ = {}
        try:
            bstack11ll111lll1_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛰ").format(e))
            pass
        logger.debug(bstack1l1_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࡖࡶ࡬ࡰࡸࡀࠠࡱࡷࡷࡣ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᛱ").format(bstack11ll111lll1_opy_))
        if bstack11ll111lll1_opy_ is not None:
            bstack11ll111lll1_opy_[bstack1l1_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛲ")] = response.headers.get(
                bstack1l1_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛳ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll111lll1_opy_[bstack1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛴ")] = response.status_code
        return bstack11ll111lll1_opy_
    @staticmethod
    def bstack11ll111ll11_opy_(bstack11ll11l1ll1_opy_):
        bstack1l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡕࡨࡲࡩࡹࠠࡢࠢࡊࡉ࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣ࡫ࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᛵ")
        bstack11ll11l1l11_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᛶ"), bstack1l1_opy_ (u"࠭ࠧᛷ"))
        headers = {
            bstack1l1_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᛸ"): bstack1l1_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫ᛹").format(bstack11ll11l1l11_opy_),
            bstack1l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ᛺"): bstack1l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭᛻")
        }
        response = requests.get(bstack11ll11l1ll1_opy_, headers=headers)
        bstack11ll111lll1_opy_ = {}
        try:
            bstack11ll111lll1_opy_ = response.json()
            logger.debug(bstack1l1_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸ࡚ࡺࡩ࡭ࡵ࠽ࠤ࡬࡫ࡴࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨ᛼").format(bstack11ll111lll1_opy_))
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤ᛽").format(e, response.text))
            pass
        if bstack11ll111lll1_opy_ is not None:
            bstack11ll111lll1_opy_[bstack1l1_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧ᛾")] = response.headers.get(
                bstack1l1_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨ᛿"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll111lll1_opy_[bstack1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜀ")] = response.status_code
        return bstack11ll111lll1_opy_
    @staticmethod
    def bstack11ll11l11ll_opy_(bstack11ll11l11l1_opy_, payload):
        bstack1l1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡍࡢ࡭ࡨࡷࠥࡧࠠࡑࡑࡖࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠠࠩࡵࡷࡶ࠮ࡀࠠࡕࡪࡨࠤࡆࡖࡉࠡࡧࡱࡨࡵࡵࡩ࡯ࡶࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡣࡼࡰࡴࡧࡤࠡࠪࡧ࡭ࡨࡺࠩ࠻ࠢࡗ࡬ࡪࠦࡲࡦࡳࡸࡩࡸࡺࠠࡱࡣࡼࡰࡴࡧࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴ࠻ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡁࡑࡋ࠯ࠤࡴࡸࠠࡏࡱࡱࡩࠥ࡯ࡦࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᜁ")
        try:
            url = bstack1l1_opy_ (u"ࠥࡿࢂ࠵ࡻࡾࠤᜂ").format(bstack11ll1ll1111_opy_, bstack11ll11l11l1_opy_)
            bstack11ll11l1l11_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᜃ"), bstack1l1_opy_ (u"ࠬ࠭ᜄ"))
            headers = {
                bstack1l1_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᜅ"): bstack1l1_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᜆ").format(bstack11ll11l1l11_opy_),
                bstack1l1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᜇ"): bstack1l1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᜈ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll111llll_opy_ = [200, 202]
            if response.status_code in bstack11ll111llll_opy_:
                return response.json()
            else:
                logger.error(bstack1l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤ࠲࡙ࠥࡴࡢࡶࡸࡷ࠿ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᜉ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡹࡴࡠࡥࡲࡰࡱ࡫ࡣࡵࡡࡥࡹ࡮ࡲࡤࡠࡦࡤࡸࡦࡀࠠࡼࡿࠥᜊ").format(e))
            return None