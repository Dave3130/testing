# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1lll11l_opy_
logger = logging.getLogger(__name__)
class bstack11ll1l1l111_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11l1111_opy_ = urljoin(builder, bstack11ll_opy_ (u"ࠨ࡫ࡶࡷࡺ࡫ࡳࠨᛏ"))
        if params:
            bstack11ll11l1111_opy_ += bstack11ll_opy_ (u"ࠤࡂࡿࢂࠨᛐ").format(urlencode({bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᛑ"): params.get(bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᛒ"))}))
        return bstack11ll1l1l111_opy_.bstack11ll111l1l1_opy_(bstack11ll11l1111_opy_)
    @staticmethod
    def bstack11ll11l1lll_opy_(builder,params=None):
        bstack11ll11l1111_opy_ = urljoin(builder, bstack11ll_opy_ (u"ࠬ࡯ࡳࡴࡷࡨࡷ࠲ࡹࡵ࡮࡯ࡤࡶࡾ࠭ᛓ"))
        if params:
            bstack11ll11l1111_opy_ += bstack11ll_opy_ (u"ࠨ࠿ࡼࡿࠥᛔ").format(urlencode({bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᛕ"): params.get(bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᛖ"))}))
        return bstack11ll1l1l111_opy_.bstack11ll111l1l1_opy_(bstack11ll11l1111_opy_)
    @staticmethod
    def bstack11ll111l1l1_opy_(bstack11ll111lll1_opy_):
        bstack11ll111llll_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᛗ"), os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᛘ"), bstack11ll_opy_ (u"ࠫࠬᛙ")))
        headers = {bstack11ll_opy_ (u"ࠬࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᛚ"): bstack11ll_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᛛ").format(bstack11ll111llll_opy_)}
        response = requests.get(bstack11ll111lll1_opy_, headers=headers)
        bstack11ll111l111_opy_ = {}
        try:
            bstack11ll111l111_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᛜ").format(e))
            pass
        if bstack11ll111l111_opy_ is not None:
            bstack11ll111l111_opy_[bstack11ll_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛝ")] = response.headers.get(bstack11ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛞ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll111l111_opy_[bstack11ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛟ")] = response.status_code
        return bstack11ll111l111_opy_
    @staticmethod
    def bstack11ll1lll1ll_opy_(bstack11ll111ll1l_opy_, data):
        logger.debug(bstack11ll_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡳࡷࠦࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡖࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࠨᛠ"))
        return bstack11ll1l1l111_opy_.bstack11ll11l11ll_opy_(bstack11ll_opy_ (u"ࠬࡖࡏࡔࡖࠪᛡ"), bstack11ll111ll1l_opy_, data=data)
    @staticmethod
    def bstack11ll1ll1l1l_opy_(bstack11ll111ll1l_opy_, data):
        logger.debug(bstack11ll_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡖࡪࡷࡵࡦࡵࡷࠤ࡫ࡵࡲࠡࡩࡨࡸ࡙࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡸࠨᛢ"))
        res = bstack11ll1l1l111_opy_.bstack11ll11l11ll_opy_(bstack11ll_opy_ (u"ࠧࡈࡇࡗࠫᛣ"), bstack11ll111ll1l_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l11ll_opy_(method, bstack11ll111ll1l_opy_, data=None, params=None, extra_headers=None):
        bstack11ll111llll_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᛤ"), bstack11ll_opy_ (u"ࠩࠪᛥ"))
        headers = {
            bstack11ll_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᛦ"): bstack11ll_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᛧ").format(bstack11ll111llll_opy_),
            bstack11ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᛨ"): bstack11ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᛩ"),
            bstack11ll_opy_ (u"ࠧࡂࡥࡦࡩࡵࡺࠧᛪ"): bstack11ll_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ᛫")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1lll11l_opy_ + bstack11ll_opy_ (u"ࠤ࠲ࠦ᛬") + bstack11ll111ll1l_opy_.lstrip(bstack11ll_opy_ (u"ࠪ࠳ࠬ᛭"))
        try:
            if method == bstack11ll_opy_ (u"ࠫࡌࡋࡔࠨᛮ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack11ll_opy_ (u"ࠬࡖࡏࡔࡖࠪᛯ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack11ll_opy_ (u"࠭ࡐࡖࡖࠪᛰ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack11ll_opy_ (u"ࠢࡖࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥࡎࡔࡕࡒࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࢀࢃࠢᛱ").format(method))
            logger.debug(bstack11ll_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡰࡥࡩ࡫ࠠࡵࡱ࡙ࠣࡗࡒ࠺ࠡࡽࢀࠤࡼ࡯ࡴࡩࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࡿࢂࠨᛲ").format(url, method))
            bstack11ll111l111_opy_ = {}
            try:
                bstack11ll111l111_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠡ࠯ࠣࡿࢂࠨᛳ").format(e, response.text))
            if bstack11ll111l111_opy_ is not None:
                bstack11ll111l111_opy_[bstack11ll_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛴ")] = response.headers.get(
                    bstack11ll_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛵ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll111l111_opy_[bstack11ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᛶ")] = response.status_code
            return bstack11ll111l111_opy_
        except Exception as e:
            logger.error(bstack11ll_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᛷ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11l11l1_opy_(bstack11ll111lll1_opy_, data):
        bstack11ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡘ࡫࡮ࡥࡵࠣࡥࠥࡖࡕࡕࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡺࡨࡦࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᛸ")
        bstack11ll111llll_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ᛹"), bstack11ll_opy_ (u"ࠩࠪ᛺"))
        headers = {
            bstack11ll_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ᛻"): bstack11ll_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧ᛼").format(bstack11ll111llll_opy_),
            bstack11ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ᛽"): bstack11ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ᛾")
        }
        response = requests.put(bstack11ll111lll1_opy_, headers=headers, json=data)
        bstack11ll111l111_opy_ = {}
        try:
            bstack11ll111l111_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨ᛿").format(e))
            pass
        logger.debug(bstack11ll_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࡗࡷ࡭ࡱࡹ࠺ࠡࡲࡸࡸࡤ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᜀ").format(bstack11ll111l111_opy_))
        if bstack11ll111l111_opy_ is not None:
            bstack11ll111l111_opy_[bstack11ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᜁ")] = response.headers.get(
                bstack11ll_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᜂ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll111l111_opy_[bstack11ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᜃ")] = response.status_code
        return bstack11ll111l111_opy_
    @staticmethod
    def bstack11ll111l1ll_opy_(bstack11ll111lll1_opy_):
        bstack11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡩࡳࡪࡳࠡࡣࠣࡋࡊ࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡬࡫ࡴࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᜄ")
        bstack11ll111llll_opy_ = os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᜅ"), bstack11ll_opy_ (u"ࠧࠨᜆ"))
        headers = {
            bstack11ll_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᜇ"): bstack11ll_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᜈ").format(bstack11ll111llll_opy_),
            bstack11ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᜉ"): bstack11ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᜊ")
        }
        response = requests.get(bstack11ll111lll1_opy_, headers=headers)
        bstack11ll111l111_opy_ = {}
        try:
            bstack11ll111l111_opy_ = response.json()
            logger.debug(bstack11ll_opy_ (u"ࠧࡘࡥࡲࡷࡨࡷࡹ࡛ࡴࡪ࡮ࡶ࠾ࠥ࡭ࡥࡵࡡࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᜋ").format(bstack11ll111l111_opy_))
        except Exception as e:
            logger.debug(bstack11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠥ࠳ࠠࡼࡿࠥᜌ").format(e, response.text))
            pass
        if bstack11ll111l111_opy_ is not None:
            bstack11ll111l111_opy_[bstack11ll_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᜍ")] = response.headers.get(
                bstack11ll_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᜎ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll111l111_opy_[bstack11ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜏ")] = response.status_code
        return bstack11ll111l111_opy_
    @staticmethod
    def bstack11ll111ll11_opy_(bstack11ll111l11l_opy_, payload):
        bstack11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡎࡣ࡮ࡩࡸࠦࡡࠡࡒࡒࡗ࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴࠡࠪࡶࡸࡷ࠯࠺ࠡࡖ࡫ࡩࠥࡇࡐࡊࠢࡨࡲࡩࡶ࡯ࡪࡰࡷࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡽࡱࡵࡡࡥࠢࠫࡨ࡮ࡩࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡲࡤࡽࡱࡵࡡࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵ࠼ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡂࡒࡌ࠰ࠥࡵࡲࠡࡐࡲࡲࡪࠦࡩࡧࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᜐ")
        try:
            url = bstack11ll_opy_ (u"ࠦࢀࢃ࠯ࡼࡿࠥᜑ").format(bstack11ll1lll11l_opy_, bstack11ll111l11l_opy_)
            bstack11ll111llll_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᜒ"), bstack11ll_opy_ (u"࠭ࠧᜓ"))
            headers = {
                bstack11ll_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴ᜔ࠧ"): bstack11ll_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀ᜕ࠫ").format(bstack11ll111llll_opy_),
                bstack11ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ᜖"): bstack11ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭᜗")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11l111l_opy_ = [200, 202]
            if response.status_code in bstack11ll11l111l_opy_:
                return response.json()
            else:
                logger.error(bstack11ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥ࠳ࠦࡓࡵࡣࡷࡹࡸࡀࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥ᜘").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡳࡵࡡࡦࡳࡱࡲࡥࡤࡶࡢࡦࡺ࡯࡬ࡥࡡࡧࡥࡹࡧ࠺ࠡࡽࢀࠦ᜙").format(e))
            return None