# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1111l1l_opy_, bstack1111ll1ll11_opy_, bstack1l1111111_opy_, error_handler, bstack1111l1lll1l_opy_, bstack1111lll1l11_opy_, bstack1111lll11l1_opy_, bstack1llll11l_opy_, bstack1lll1l11_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11ll1111_opy_ import bstack111ll1l1111_opy_
import bstack_utils.bstack11ll11ll1_opy_ as bstack1l1lll1l1l_opy_
from bstack_utils.bstack1ll1ll1l_opy_ import bstack1llll111_opy_
import bstack_utils.accessibility as bstack1lll1lll1_opy_
from bstack_utils.bstack1llll11l11_opy_ import bstack1llll11l11_opy_
from bstack_utils.bstack1ll11lll_opy_ import bstack1l11l111_opy_
from bstack_utils.constants import bstack1l11l1lll1_opy_
bstack1llll11lll1l_opy_ = bstack1lllll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡨࡵ࡬࡭ࡧࡦࡸࡴࡸ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ⃽")
logger = logging.getLogger(__name__)
class bstack1ll111ll_opy_:
    bstack11l11ll1111_opy_ = None
    bs_config = None
    bstack1llll111l1_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l11l1ll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def launch(cls, bs_config, bstack1llll111l1_opy_):
        cls.bs_config = bs_config
        cls.bstack1llll111l1_opy_ = bstack1llll111l1_opy_
        try:
            cls.bstack1llll1ll1111_opy_()
            bstack1lllll11l1ll_opy_ = bstack111l1111l1l_opy_(bs_config)
            bstack1lllll11111l_opy_ = bstack1111ll1ll11_opy_(bs_config)
            data = bstack1l1lll1l1l_opy_.bstack1llll1l11lll_opy_(bs_config, bstack1llll111l1_opy_)
            config = {
                bstack1lllll1_opy_ (u"ࠫࡦࡻࡴࡩࠩ⃾"): (bstack1lllll11l1ll_opy_, bstack1lllll11111l_opy_),
                bstack1lllll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭⃿"): cls.default_headers()
            }
            response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"࠭ࡐࡐࡕࡗࠫ℀"), cls.request_url(bstack1lllll1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠸࠯ࡣࡷ࡬ࡰࡩࡹࠧ℁")), data, config)
            if response.status_code != 200:
                bstack1l11ll1l1l_opy_ = response.json()
                if bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩℂ")] == False:
                    cls.bstack1llll1l1l11l_opy_(bstack1l11ll1l1l_opy_)
                    return
                cls.bstack1llll1l1ll11_opy_(bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ℃")])
                cls.bstack1llll1l1ll1l_opy_(bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ℄")])
                return None
            bstack1llll1l1l1ll_opy_ = cls.bstack1llll1ll111l_opy_(response)
            return bstack1llll1l1l1ll_opy_, response.json()
        except Exception as error:
            logger.error(bstack1lllll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡧࡱࡵࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࡻࡾࠤ℅").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l1111l_opy_=None):
        if not bstack1llll111_opy_.on() and not bstack1lll1lll1_opy_.on():
            return
        if os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ℆")) == bstack1lllll1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦℇ") or os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ℈")) == bstack1lllll1_opy_ (u"ࠣࡰࡸࡰࡱࠨ℉"):
            logger.error(bstack1lllll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬℊ"))
            return {
                bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪℋ"): bstack1lllll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪℌ"),
                bstack1lllll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ℍ"): bstack1lllll1_opy_ (u"࠭ࡔࡰ࡭ࡨࡲ࠴ࡨࡵࡪ࡮ࡧࡍࡉࠦࡩࡴࠢࡸࡲࡩ࡫ࡦࡪࡰࡨࡨ࠱ࠦࡢࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠ࡮࡫ࡪ࡬ࡹࠦࡨࡢࡸࡨࠤ࡫ࡧࡩ࡭ࡧࡧࠫℎ")
            }
        try:
            cls.bstack11l11ll1111_opy_.shutdown()
            data = {
                bstack1lllll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬℏ"): bstack1llll11l_opy_()
            }
            if not bstack1llll1l1111l_opy_ is None:
                data[bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡱࡪࡺࡡࡥࡣࡷࡥࠬℐ")] = [{
                    bstack1lllll1_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩℑ"): bstack1lllll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡠ࡭࡬ࡰࡱ࡫ࡤࠨℒ"),
                    bstack1lllll1_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࠫℓ"): bstack1llll1l1111l_opy_
                }]
            config = {
                bstack1lllll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭℔"): cls.default_headers()
            }
            bstack11ll11l1ll1_opy_ = bstack1lllll1_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡸࡴࡶࠧℕ").format(os.environ[bstack1lllll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧ№")])
            bstack1llll1l1l1l1_opy_ = cls.request_url(bstack11ll11l1ll1_opy_)
            response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠨࡒࡘࡘࠬ℗"), bstack1llll1l1l1l1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1lllll1_opy_ (u"ࠤࡖࡸࡴࡶࠠࡳࡧࡴࡹࡪࡹࡴࠡࡰࡲࡸࠥࡵ࡫ࠣ℘"))
        except Exception as error:
            logger.error(bstack1lllll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾࠿ࠦࠢℙ") + str(error))
            return {
                bstack1lllll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫℚ"): bstack1lllll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫℛ"),
                bstack1lllll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧℜ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1ll111l_opy_(cls, response):
        bstack1l11ll1l1l_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l1l1ll_opy_ = {}
        if bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠧ࡫ࡹࡷࠫℝ")) is None:
            os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ℞")] = bstack1lllll1_opy_ (u"ࠩࡱࡹࡱࡲࠧ℟")
        else:
            os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ℠")] = bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠫ࡯ࡽࡴࠨ℡"), bstack1lllll1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ™"))
        os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ℣")] = bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩℤ"), bstack1lllll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭℥"))
        logger.info(bstack1lllll1_opy_ (u"ࠩࡗࡩࡸࡺࡨࡶࡤࠣࡷࡹࡧࡲࡵࡧࡧࠤࡼ࡯ࡴࡩࠢ࡬ࡨ࠿ࠦࠧΩ") + os.getenv(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ℧")));
        if bstack1llll111_opy_.bstack11l11l1ll1l_opy_(cls.bs_config, cls.bstack1llll111l1_opy_.get(bstack1lllll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬℨ"), bstack1lllll1_opy_ (u"ࠬ࠭℩"))) is True:
            bstack11ll11ll1ll_opy_, build_hashed_id, bstack1llll11ll1ll_opy_ = cls.bstack1llll1l111ll_opy_(bstack1l11ll1l1l_opy_)
            if bstack11ll11ll1ll_opy_ != None and build_hashed_id != None:
                bstack1llll1l1l1ll_opy_[bstack1lllll1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭K")] = {
                    bstack1lllll1_opy_ (u"ࠧ࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠪÅ"): bstack11ll11ll1ll_opy_,
                    bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪℬ"): build_hashed_id,
                    bstack1lllll1_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ℭ"): bstack1llll11ll1ll_opy_
                }
            else:
                bstack1llll1l1l1ll_opy_[bstack1lllll1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ℮")] = {}
        else:
            bstack1llll1l1l1ll_opy_[bstack1lllll1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫℯ")] = {}
        bstack1llll1ll11l1_opy_, build_hashed_id = cls.bstack1llll1l1l111_opy_(bstack1l11ll1l1l_opy_)
        if bstack1llll1ll11l1_opy_ != None and build_hashed_id != None:
            bstack1llll1l1l1ll_opy_[bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬℰ")] = {
                bstack1lllll1_opy_ (u"࠭ࡡࡶࡶ࡫ࡣࡹࡵ࡫ࡦࡰࠪℱ"): bstack1llll1ll11l1_opy_,
                bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩℲ"): build_hashed_id,
            }
        else:
            bstack1llll1l1l1ll_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨℳ")] = {}
        if bstack1llll1l1l1ll_opy_[bstack1lllll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩℴ")].get(bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬℵ")) != None or bstack1llll1l1l1ll_opy_[bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℶ")].get(bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧℷ")) != None:
            cls.bstack1llll1l1llll_opy_(bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"࠭ࡪࡸࡶࠪℸ")), bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩℹ")))
        return bstack1llll1l1l1ll_opy_
    @classmethod
    def bstack1llll1l111ll_opy_(cls, bstack1l11ll1l1l_opy_):
        if bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ℺")) == None:
            cls.bstack1llll1l1ll11_opy_()
            return [None, None, None]
        if bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ℻")][bstack1lllll1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫℼ")] != True:
            cls.bstack1llll1l1ll11_opy_(bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫℽ")])
            return [None, None, None]
        logger.debug(bstack1lllll1_opy_ (u"ࠬࢁࡽࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧℾ").format(bstack1l11l1lll1_opy_))
        os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬℿ")] = bstack1lllll1_opy_ (u"ࠧࡵࡴࡸࡩࠬ⅀")
        if bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠨ࡬ࡺࡸࠬ⅁")):
            os.environ[bstack1lllll1_opy_ (u"ࠩࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙࡟ࡇࡑࡕࡣࡈࡘࡁࡔࡊࡢࡖࡊࡖࡏࡓࡖࡌࡒࡌ࠭⅂")] = json.dumps({
                bstack1lllll1_opy_ (u"ࠪࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ⅃"): bstack111l1111l1l_opy_(cls.bs_config),
                bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭⅄"): bstack1111ll1ll11_opy_(cls.bs_config)
            })
        if bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧⅅ")):
            os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬⅆ")] = bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅇ")]
        if bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨⅈ")].get(bstack1lllll1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪⅉ"), {}).get(bstack1lllll1_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ⅊")):
            os.environ[bstack1lllll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ⅋")] = str(bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅌")][bstack1lllll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ⅍")][bstack1lllll1_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫⅎ")])
        else:
            os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩ⅏")] = bstack1lllll1_opy_ (u"ࠤࡱࡹࡱࡲࠢ⅐")
        return [bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠪ࡮ࡼࡺࠧ⅑")], bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅒")], os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭⅓")]]
    @classmethod
    def bstack1llll1l1l111_opy_(cls, bstack1l11ll1l1l_opy_):
        if bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅔")) == None:
            cls.bstack1llll1l1ll1l_opy_()
            return [None, None]
        if bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⅕")][bstack1lllll1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ⅖")] != True:
            cls.bstack1llll1l1ll1l_opy_(bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")])
            return [None, None]
        if bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⅘")].get(bstack1lllll1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ⅙")):
            logger.debug(bstack1lllll1_opy_ (u"࡚ࠬࡥࡴࡶࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠢࠩ⅚"))
            parsed = json.loads(os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ⅛"), bstack1lllll1_opy_ (u"ࠧࡼࡿࠪ⅜")))
            capabilities = bstack1l1lll1l1l_opy_.bstack1llll1l111l1_opy_(bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⅝")][bstack1lllll1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ⅞")][bstack1lllll1_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⅟")], bstack1lllll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩⅠ"), bstack1lllll1_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫⅡ"))
            bstack1llll1ll11l1_opy_ = capabilities[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫⅢ")]
            os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬⅣ")] = bstack1llll1ll11l1_opy_
            if bstack1lllll1_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥⅤ") in bstack1l11ll1l1l_opy_ and bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠤࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠣⅥ")) is None:
                parsed[bstack1lllll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫⅦ")] = capabilities[bstack1lllll1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬⅧ")]
            os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭Ⅸ")] = json.dumps(parsed)
            scripts = bstack1l1lll1l1l_opy_.bstack1llll1l111l1_opy_(bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭Ⅹ")][bstack1lllll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅪ")][bstack1lllll1_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩⅫ")], bstack1lllll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧⅬ"), bstack1lllll1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࠫⅭ"))
            bstack1llll11l11_opy_.bstack1111l1111_opy_(scripts)
            commands = bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫⅮ")][bstack1lllll1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭Ⅿ")][bstack1lllll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࡕࡱ࡚ࡶࡦࡶࠧⅰ")].get(bstack1lllll1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩⅱ"))
            bstack1llll11l11_opy_.bstack1lllll1l11ll_opy_(commands)
            bstack1lllll1l1l1l_opy_ = capabilities.get(bstack1lllll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ⅲ"))
            bstack1llll11l11_opy_.bstack1lllll1l1l11_opy_(bstack1lllll1l1l1l_opy_)
            bstack1llll11l11_opy_.store()
        return [bstack1llll1ll11l1_opy_, bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫⅳ")]]
    @classmethod
    def bstack1llll1l1ll11_opy_(cls, response=None):
        os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨⅴ")] = bstack1lllll1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩⅵ")
        os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩⅶ")] = bstack1lllll1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫⅷ")
        os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭ⅸ")] = bstack1lllll1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧⅹ")
        os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨⅺ")] = bstack1lllll1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣⅻ")
        os.environ[bstack1lllll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬⅼ")] = bstack1lllll1_opy_ (u"ࠧࡴࡵ࡭࡮ࠥⅽ")
        cls.bstack1llll1l1l11l_opy_(response, bstack1lllll1_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨⅾ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l1ll1l_opy_(cls, response=None):
        os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬⅿ")] = bstack1lllll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ↀ")
        os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧↁ")] = bstack1lllll1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨↂ")
        os.environ[bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨↃ")] = bstack1lllll1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪↄ")
        cls.bstack1llll1l1l11l_opy_(response, bstack1lllll1_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠨↅ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l1llll_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫↆ")] = jwt
        os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ↇ")] = build_hashed_id
    @classmethod
    def bstack1llll1l1l11l_opy_(cls, response=None, product=bstack1lllll1_opy_ (u"ࠤࠥↈ")):
        if response == None or response.get(bstack1lllll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪ↉")) == None:
            logger.error(product + bstack1lllll1_opy_ (u"ࠦࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠨ↊"))
            return
        for error in response[bstack1lllll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ↋")]:
            bstack111l11l1l1l_opy_ = error[bstack1lllll1_opy_ (u"࠭࡫ࡦࡻࠪ↌")]
            error_message = error[bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ↍")]
            if error_message:
                if bstack111l11l1l1l_opy_ == bstack1lllll1_opy_ (u"ࠣࡇࡕࡖࡔࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡅࡇࡑࡍࡊࡊࠢ↎"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1lllll1_opy_ (u"ࠤࡇࡥࡹࡧࠠࡶࡲ࡯ࡳࡦࡪࠠࡵࡱࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࠥ↏") + product + bstack1lllll1_opy_ (u"ࠥࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣ←"))
    @classmethod
    def bstack1llll1ll1111_opy_(cls):
        if cls.bstack11l11ll1111_opy_ is not None:
            return
        cls.bstack11l11ll1111_opy_ = bstack111ll1l1111_opy_(cls.post_data)
        cls.bstack11l11ll1111_opy_.start()
    @classmethod
    def bstack1l1l11l1_opy_(cls):
        if cls.bstack11l11ll1111_opy_ is None:
            return
        cls.bstack11l11ll1111_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l1lll1l_opy_, event_url=bstack1lllll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ↑")):
        config = {
            bstack1lllll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭→"): cls.default_headers()
        }
        logger.debug(bstack1lllll1_opy_ (u"ࠨࡰࡰࡵࡷࡣࡩࡧࡴࡢ࠼ࠣࡗࡪࡴࡤࡪࡰࡪࠤࡩࡧࡴࡢࠢࡷࡳࠥࡺࡥࡴࡶ࡫ࡹࡧࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࡵࠣࡿࢂࠨ↓").format(bstack1lllll1_opy_ (u"ࠧ࠭ࠢࠪ↔").join([event[bstack1lllll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↕")] for event in bstack1l1lll1l_opy_])))
        response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ↖"), cls.request_url(event_url), bstack1l1lll1l_opy_, config)
        bstack1llll1ll1l11_opy_ = response.json()
    @classmethod
    def bstack1l1l111l_opy_(cls, bstack1l1lll1l_opy_, event_url=bstack1lllll1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ↗")):
        logger.debug(bstack1lllll1_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡣࡧࡨࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ↘").format(bstack1l1lll1l_opy_[bstack1lllll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↙")]))
        if not bstack1l1lll1l1l_opy_.bstack1llll1l1lll1_opy_(bstack1l1lll1l_opy_[bstack1lllll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↚")]):
            logger.debug(bstack1lllll1_opy_ (u"ࠢࡴࡧࡱࡨࡤࡪࡡࡵࡣ࠽ࠤࡓࡵࡴࠡࡣࡧࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ↛").format(bstack1l1lll1l_opy_[bstack1lllll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↜")]))
            return
        bstack1l1l1l1l11_opy_ = bstack1l1lll1l1l_opy_.bstack1llll11llll1_opy_(bstack1l1lll1l_opy_[bstack1lllll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↝")], bstack1l1lll1l_opy_.get(bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ↞")))
        if bstack1l1l1l1l11_opy_ != None:
            if bstack1l1lll1l_opy_.get(bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭↟")) != None:
                bstack1l1lll1l_opy_[bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ↠")][bstack1lllll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ↡")] = bstack1l1l1l1l11_opy_
            else:
                bstack1l1lll1l_opy_[bstack1lllll1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ↢")] = bstack1l1l1l1l11_opy_
        if event_url == bstack1lllll1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ↣"):
            cls.bstack1llll1ll1111_opy_()
            logger.debug(bstack1lllll1_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡁࡥࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ↤").format(bstack1l1lll1l_opy_[bstack1lllll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↥")]))
            cls.bstack11l11ll1111_opy_.add(bstack1l1lll1l_opy_)
        elif event_url == bstack1lllll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ↦"):
            cls.post_data([bstack1l1lll1l_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l11l1l1_opy_(cls, logs):
        for log in logs:
            bstack1llll11lllll_opy_ = {
                bstack1lllll1_opy_ (u"ࠬࡱࡩ࡯ࡦࠪ↧"): bstack1lllll1_opy_ (u"࠭ࡔࡆࡕࡗࡣࡑࡕࡇࠨ↨"),
                bstack1lllll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭↩"): log[bstack1lllll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ↪")],
                bstack1lllll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ↫"): log[bstack1lllll1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭↬")],
                bstack1lllll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡡࡵࡩࡸࡶ࡯࡯ࡵࡨࠫ↭"): {},
                bstack1lllll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭↮"): log[bstack1lllll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ↯")],
            }
            if bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↰") in log:
                bstack1llll11lllll_opy_[bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↱")] = log[bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ↲")]
            elif bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↳") in log:
                bstack1llll11lllll_opy_[bstack1lllll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↴")] = log[bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↵")]
            cls.bstack1l1l111l_opy_({
                bstack1lllll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↶"): bstack1lllll1_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ↷"),
                bstack1lllll1_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭↸"): [bstack1llll11lllll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l11ll1_opy_(cls, steps):
        bstack1llll1l11l11_opy_ = []
        for step in steps:
            bstack1llll1l11l1l_opy_ = {
                bstack1lllll1_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ↹"): bstack1lllll1_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡗࡉࡕ࠭↺"),
                bstack1lllll1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ↻"): step[bstack1lllll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ↼")],
                bstack1lllll1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ↽"): step[bstack1lllll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ↾")],
                bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↿"): step[bstack1lllll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇀")],
                bstack1lllll1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ⇁"): step[bstack1lllll1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⇂")]
            }
            if bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇃") in step:
                bstack1llll1l11l1l_opy_[bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇄")] = step[bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇅")]
            elif bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇆") in step:
                bstack1llll1l11l1l_opy_[bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇇")] = step[bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇈")]
            bstack1llll1l11l11_opy_.append(bstack1llll1l11l1l_opy_)
        cls.bstack1l1l111l_opy_({
            bstack1lllll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇉"): bstack1lllll1_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ⇊"),
            bstack1lllll1_opy_ (u"࠭࡬ࡰࡩࡶࠫ⇋"): bstack1llll1l11l11_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1l11lll11l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack11111l1ll1_opy_(cls, screenshot):
        cls.bstack1l1l111l_opy_({
            bstack1lllll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇌"): bstack1lllll1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⇍"),
            bstack1lllll1_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ⇎"): [{
                bstack1lllll1_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ⇏"): bstack1lllll1_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࠭⇐"),
                bstack1lllll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ⇑"): datetime.datetime.utcnow().isoformat() + bstack1lllll1_opy_ (u"࡚࠭ࠨ⇒"),
                bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇓"): screenshot[bstack1lllll1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ⇔")],
                bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇕"): screenshot[bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇖")]
            }]
        }, event_url=bstack1lllll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ⇗"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1111ll1l1l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l1l111l_opy_({
            bstack1lllll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇘"): bstack1lllll1_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ⇙"),
            bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ⇚"): {
                bstack1lllll1_opy_ (u"ࠣࡷࡸ࡭ࡩࠨ⇛"): cls.current_test_uuid(),
                bstack1lllll1_opy_ (u"ࠤ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠣ⇜"): cls.bstack1l1l1l1l_opy_(driver)
            }
        })
    @classmethod
    def bstack11lll1l1_opy_(cls, event: str, bstack1l1lll1l_opy_: bstack1l11l111_opy_):
        bstack1l111l11_opy_ = {
            bstack1lllll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇝"): event,
            bstack1l1lll1l_opy_.event_key(): bstack1l1lll1l_opy_.bstack1lll11ll_opy_(event)
        }
        cls.bstack1l1l111l_opy_(bstack1l111l11_opy_)
        result = getattr(bstack1l1lll1l_opy_, bstack1lllll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⇞"), None)
        if event == bstack1lllll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⇟"):
            threading.current_thread().bstackTestMeta = {bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⇠"): bstack1lllll1_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ⇡")}
        elif event == bstack1lllll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⇢"):
            threading.current_thread().bstackTestMeta = {bstack1lllll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⇣"): getattr(result, bstack1lllll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⇤"), bstack1lllll1_opy_ (u"ࠫࠬ⇥"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⇦"), None) is None or os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ⇧")] == bstack1lllll1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ⇨")) and (os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭⇩"), None) is None or os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ⇪")] == bstack1lllll1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ⇫")):
            return False
        return True
    @staticmethod
    def bstack1llll11lll11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll111ll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1lllll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ⇬"): bstack1lllll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ⇭"),
            bstack1lllll1_opy_ (u"࠭ࡘ࠮ࡄࡖࡘࡆࡉࡋ࠮ࡖࡈࡗ࡙ࡕࡐࡔࠩ⇮"): bstack1lllll1_opy_ (u"ࠧࡵࡴࡸࡩࠬ⇯")
        }
        if os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ⇰"), None):
            headers[bstack1lllll1_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ⇱")] = bstack1lllll1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭⇲").format(os.environ[bstack1lllll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠣ⇳")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1lllll1_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫ⇴").format(bstack1llll11lll1l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ⇵"), None)
    @staticmethod
    def bstack1l1l1l1l_opy_(driver):
        return {
            bstack1111l1lll1l_opy_(): bstack1111lll1l11_opy_(driver)
        }
    @staticmethod
    def bstack1llll1l11111_opy_(exception_info, report):
        return [{bstack1lllll1_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪ⇶"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111l11ll_opy_(typename):
        if bstack1lllll1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦ⇷") in typename:
            return bstack1lllll1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥ⇸")
        return bstack1lllll1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦ⇹")