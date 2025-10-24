# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1111ll11111_opy_, bstack1111ll1l111_opy_, bstack1ll1l1l11l_opy_, error_handler, bstack111l11ll11l_opy_, bstack111l1l11lll_opy_, bstack1111llll11l_opy_, bstack1l11ll1l_opy_, bstack1ll11l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l11l1l_opy_ import bstack111l1llll1l_opy_
import bstack_utils.bstack1l11l11l11_opy_ as bstack1l1l1ll111_opy_
from bstack_utils.bstack1ll1ll1l_opy_ import bstack1ll1l1l1_opy_
import bstack_utils.accessibility as bstack111llll1_opy_
from bstack_utils.bstack1lllll111l_opy_ import bstack1lllll111l_opy_
from bstack_utils.bstack1ll1llll_opy_ import bstack1l11ll11_opy_
from bstack_utils.constants import bstack11ll1l1ll1_opy_
bstack1llll11ll1l1_opy_ = bstack11l11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡩ࡯࡭࡮ࡨࡧࡹࡵࡲ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫℓ")
logger = logging.getLogger(__name__)
class bstack1l11l111_opy_:
    bstack11l11l11l1l_opy_ = None
    bs_config = None
    bstack111llllll1_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11ll1ll1_opy_, stage=STAGE.bstack1ll1lllll_opy_)
    def launch(cls, bs_config, bstack111llllll1_opy_):
        cls.bs_config = bs_config
        cls.bstack111llllll1_opy_ = bstack111llllll1_opy_
        try:
            cls.bstack1llll11l11ll_opy_()
            bstack1lllll111l1l_opy_ = bstack1111ll11111_opy_(bs_config)
            bstack1llll1llll11_opy_ = bstack1111ll1l111_opy_(bs_config)
            data = bstack1l1l1ll111_opy_.bstack1llll11llll1_opy_(bs_config, bstack111llllll1_opy_)
            config = {
                bstack11l11l1_opy_ (u"ࠬࡧࡵࡵࡪࠪ℔"): (bstack1lllll111l1l_opy_, bstack1llll1llll11_opy_),
                bstack11l11l1_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧℕ"): cls.default_headers()
            }
            response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠧࡑࡑࡖࡘࠬ№"), cls.request_url(bstack11l11l1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠲࠰ࡤࡸ࡭ࡱࡪࡳࠨ℗")), data, config)
            if response.status_code != 200:
                bstack11l1l11l11_opy_ = response.json()
                if bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ℘")] == False:
                    cls.bstack1llll11l1l1l_opy_(bstack11l1l11l11_opy_)
                    return
                cls.bstack1llll11ll1ll_opy_(bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪℙ")])
                cls.bstack1llll1l11l1l_opy_(bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℚ")])
                return None
            bstack1llll11lllll_opy_ = cls.bstack1llll11l1l11_opy_(response)
            return bstack1llll11lllll_opy_, response.json()
        except Exception as error:
            logger.error(bstack11l11l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡼࡿࠥℛ").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll11ll111_opy_=None):
        if not bstack1ll1l1l1_opy_.on() and not bstack111llll1_opy_.on():
            return
        if os.environ.get(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪℜ")) == bstack11l11l1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧℝ") or os.environ.get(bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭℞")) == bstack11l11l1_opy_ (u"ࠤࡱࡹࡱࡲࠢ℟"):
            logger.error(bstack11l11l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭℠"))
            return {
                bstack11l11l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ℡"): bstack11l11l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ™"),
                bstack11l11l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ℣"): bstack11l11l1_opy_ (u"ࠧࡕࡱ࡮ࡩࡳ࠵ࡢࡶ࡫࡯ࡨࡎࡊࠠࡪࡵࠣࡹࡳࡪࡥࡧ࡫ࡱࡩࡩ࠲ࠠࡣࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡ࡯࡬࡫࡭ࡺࠠࡩࡣࡹࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠬℤ")
            }
        try:
            cls.bstack11l11l11l1l_opy_.shutdown()
            data = {
                bstack11l11l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭℥"): bstack1l11ll1l_opy_()
            }
            if not bstack1llll11ll111_opy_ is None:
                data[bstack11l11l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡲ࡫ࡴࡢࡦࡤࡸࡦ࠭Ω")] = [{
                    bstack11l11l1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ℧"): bstack11l11l1_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩℨ"),
                    bstack11l11l1_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬ℩"): bstack1llll11ll111_opy_
                }]
            config = {
                bstack11l11l1_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧK"): cls.default_headers()
            }
            bstack11ll11l1l11_opy_ = bstack11l11l1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨÅ").format(os.environ[bstack11l11l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨℬ")])
            bstack1llll1l11ll1_opy_ = cls.request_url(bstack11ll11l1l11_opy_)
            response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠩࡓ࡙࡙࠭ℭ"), bstack1llll1l11ll1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11l11l1_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤ℮"))
        except Exception as error:
            logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࡀࠠࠣℯ") + str(error))
            return {
                bstack11l11l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬℰ"): bstack11l11l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬℱ"),
                bstack11l11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨℲ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l1l11_opy_(cls, response):
        bstack11l1l11l11_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11lllll_opy_ = {}
        if bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠨ࡬ࡺࡸࠬℳ")) is None:
            os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ℴ")] = bstack11l11l1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨℵ")
        else:
            os.environ[bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨℶ")] = bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠬࡰࡷࡵࠩℷ"), bstack11l11l1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫℸ"))
        os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬℹ")] = bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ℺"), bstack11l11l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ℻"))
        logger.info(bstack11l11l1_opy_ (u"ࠪࡘࡪࡹࡴࡩࡷࡥࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࠨℼ") + os.getenv(bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩℽ")));
        if bstack1ll1l1l1_opy_.bstack11l11l11111_opy_(cls.bs_config, cls.bstack111llllll1_opy_.get(bstack11l11l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭ℾ"), bstack11l11l1_opy_ (u"࠭ࠧℿ"))) is True:
            bstack11ll11l1l1l_opy_, build_hashed_id, bstack1llll11lll11_opy_ = cls.bstack1llll1l1111l_opy_(bstack11l1l11l11_opy_)
            if bstack11ll11l1l1l_opy_ != None and build_hashed_id != None:
                bstack1llll11lllll_opy_[bstack11l11l1_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ⅀")] = {
                    bstack11l11l1_opy_ (u"ࠨ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠫ⅁"): bstack11ll11l1l1l_opy_,
                    bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⅂"): build_hashed_id,
                    bstack11l11l1_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ⅃"): bstack1llll11lll11_opy_
                }
            else:
                bstack1llll11lllll_opy_[bstack11l11l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⅄")] = {}
        else:
            bstack1llll11lllll_opy_[bstack11l11l1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅅ")] = {}
        bstack1llll11lll1l_opy_, build_hashed_id = cls.bstack1llll1l1l11l_opy_(bstack11l1l11l11_opy_)
        if bstack1llll11lll1l_opy_ != None and build_hashed_id != None:
            bstack1llll11lllll_opy_[bstack11l11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ⅆ")] = {
                bstack11l11l1_opy_ (u"ࠧࡢࡷࡷ࡬ࡤࡺ࡯࡬ࡧࡱࠫⅇ"): bstack1llll11lll1l_opy_,
                bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅈ"): build_hashed_id,
            }
        else:
            bstack1llll11lllll_opy_[bstack11l11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩⅉ")] = {}
        if bstack1llll11lllll_opy_[bstack11l11l1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅊")].get(bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅋")) != None or bstack1llll11lllll_opy_[bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅌")].get(bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⅍")) != None:
            cls.bstack1llll1l111ll_opy_(bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠧ࡫ࡹࡷࠫⅎ")), bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅏")))
        return bstack1llll11lllll_opy_
    @classmethod
    def bstack1llll1l1111l_opy_(cls, bstack11l1l11l11_opy_):
        if bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅐")) == None:
            cls.bstack1llll11ll1ll_opy_()
            return [None, None, None]
        if bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅑")][bstack11l11l1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ⅒")] != True:
            cls.bstack1llll11ll1ll_opy_(bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅓")])
            return [None, None, None]
        logger.debug(bstack11l11l1_opy_ (u"࠭ࡻࡾࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨ⅔").format(bstack11ll1l1ll1_opy_))
        os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭⅕")] = bstack11l11l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭⅖")
        if bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠩ࡭ࡻࡹ࠭⅗")):
            os.environ[bstack11l11l1_opy_ (u"ࠪࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࡠࡈࡒࡖࡤࡉࡒࡂࡕࡋࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧ⅘")] = json.dumps({
                bstack11l11l1_opy_ (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪ࠭⅙"): bstack1111ll11111_opy_(cls.bs_config),
                bstack11l11l1_opy_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧ⅚"): bstack1111ll1l111_opy_(cls.bs_config)
            })
        if bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⅛")):
            os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭⅜")] = bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅝")]
        if bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅞")].get(bstack11l11l1_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅟"), {}).get(bstack11l11l1_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨⅠ")):
            os.environ[bstack11l11l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭Ⅱ")] = str(bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭Ⅲ")][bstack11l11l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅣ")][bstack11l11l1_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬⅤ")])
        else:
            os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪⅥ")] = bstack11l11l1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣⅦ")
        return [bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠫ࡯ࡽࡴࠨⅧ")], bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧⅨ")], os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧⅩ")]]
    @classmethod
    def bstack1llll1l1l11l_opy_(cls, bstack11l1l11l11_opy_):
        if bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅪ")) == None:
            cls.bstack1llll1l11l1l_opy_()
            return [None, None]
        if bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅫ")][bstack11l11l1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪⅬ")] != True:
            cls.bstack1llll1l11l1l_opy_(bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅭ")])
            return [None, None]
        if bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫⅮ")].get(bstack11l11l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭Ⅿ")):
            logger.debug(bstack11l11l1_opy_ (u"࠭ࡔࡦࡵࡷࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪⅰ"))
            parsed = json.loads(os.getenv(bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨⅱ"), bstack11l11l1_opy_ (u"ࠨࡽࢀࠫⅲ")))
            capabilities = bstack1l1l1ll111_opy_.bstack1llll11l11l1_opy_(bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩⅳ")][bstack11l11l1_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫⅴ")][bstack11l11l1_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪⅵ")], bstack11l11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪⅶ"), bstack11l11l1_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬⅷ"))
            bstack1llll11lll1l_opy_ = capabilities[bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬⅸ")]
            os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ⅹ")] = bstack1llll11lll1l_opy_
            if bstack11l11l1_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦⅺ") in bstack11l1l11l11_opy_ and bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤⅻ")) is None:
                parsed[bstack11l11l1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬⅼ")] = capabilities[bstack11l11l1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ⅽ")]
            os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧⅾ")] = json.dumps(parsed)
            scripts = bstack1l1l1ll111_opy_.bstack1llll11l11l1_opy_(bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅿ")][bstack11l11l1_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩↀ")][bstack11l11l1_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪↁ")], bstack11l11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨↂ"), bstack11l11l1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࠬↃ"))
            bstack1lllll111l_opy_.bstack1ll111ll1_opy_(scripts)
            commands = bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬↄ")][bstack11l11l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧↅ")][bstack11l11l1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠨↆ")].get(bstack11l11l1_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪↇ"))
            bstack1lllll111l_opy_.bstack1lllll111lll_opy_(commands)
            bstack1lllll11l1l1_opy_ = capabilities.get(bstack11l11l1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧↈ"))
            bstack1lllll111l_opy_.bstack1lllll11l1ll_opy_(bstack1lllll11l1l1_opy_)
            bstack1lllll111l_opy_.store()
        return [bstack1llll11lll1l_opy_, bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ↉")]]
    @classmethod
    def bstack1llll11ll1ll_opy_(cls, response=None):
        os.environ[bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ↊")] = bstack11l11l1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ↋")
        os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ↌")] = bstack11l11l1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ↍")
        os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧ↎")] = bstack11l11l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ↏")
        os.environ[bstack11l11l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ←")] = bstack11l11l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ↑")
        os.environ[bstack11l11l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭→")] = bstack11l11l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ↓")
        cls.bstack1llll11l1l1l_opy_(response, bstack11l11l1_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢ↔"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l11l1l_opy_(cls, response=None):
        os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭↕")] = bstack11l11l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ↖")
        os.environ[bstack11l11l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ↗")] = bstack11l11l1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ↘")
        os.environ[bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ↙")] = bstack11l11l1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ↚")
        cls.bstack1llll11l1l1l_opy_(response, bstack11l11l1_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢ↛"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l111ll_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ↜")] = jwt
        os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ↝")] = build_hashed_id
    @classmethod
    def bstack1llll11l1l1l_opy_(cls, response=None, product=bstack11l11l1_opy_ (u"ࠥࠦ↞")):
        if response == None or response.get(bstack11l11l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ↟")) == None:
            logger.error(product + bstack11l11l1_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢ↠"))
            return
        for error in response[bstack11l11l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭↡")]:
            bstack1111ll11l1l_opy_ = error[bstack11l11l1_opy_ (u"ࠧ࡬ࡧࡼࠫ↢")]
            error_message = error[bstack11l11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↣")]
            if error_message:
                if bstack1111ll11l1l_opy_ == bstack11l11l1_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣ↤"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11l11l1_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦ↥") + product + bstack11l11l1_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤ↦"))
    @classmethod
    def bstack1llll11l11ll_opy_(cls):
        if cls.bstack11l11l11l1l_opy_ is not None:
            return
        cls.bstack11l11l11l1l_opy_ = bstack111l1llll1l_opy_(cls.post_data)
        cls.bstack11l11l11l1l_opy_.start()
    @classmethod
    def bstack1l11lll1_opy_(cls):
        if cls.bstack11l11l11l1l_opy_ is None:
            return
        cls.bstack11l11l11l1l_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1lll11l1_opy_, event_url=bstack11l11l1_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ↧")):
        config = {
            bstack11l11l1_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ↨"): cls.default_headers()
        }
        logger.debug(bstack11l11l1_opy_ (u"ࠢࡱࡱࡶࡸࡤࡪࡡࡵࡣ࠽ࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡶࠤࢀࢃࠢ↩").format(bstack11l11l1_opy_ (u"ࠨ࠮ࠣࠫ↪").join([event[bstack11l11l1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↫")] for event in bstack1lll11l1_opy_])))
        response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ↬"), cls.request_url(event_url), bstack1lll11l1_opy_, config)
        bstack1llll1ll11ll_opy_ = response.json()
    @classmethod
    def bstack1l1ll111_opy_(cls, bstack1lll11l1_opy_, event_url=bstack11l11l1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ↭")):
        logger.debug(bstack11l11l1_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡤࡨࡩࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ↮").format(bstack1lll11l1_opy_[bstack11l11l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↯")]))
        if not bstack1l1l1ll111_opy_.bstack1llll1l11111_opy_(bstack1lll11l1_opy_[bstack11l11l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↰")]):
            logger.debug(bstack11l11l1_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡔ࡯ࡵࠢࡤࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ↱").format(bstack1lll11l1_opy_[bstack11l11l1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↲")]))
            return
        bstack111ll11ll1_opy_ = bstack1l1l1ll111_opy_.bstack1llll11ll11l_opy_(bstack1lll11l1_opy_[bstack11l11l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↳")], bstack1lll11l1_opy_.get(bstack11l11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭↴")))
        if bstack111ll11ll1_opy_ != None:
            if bstack1lll11l1_opy_.get(bstack11l11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ↵")) != None:
                bstack1lll11l1_opy_[bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ↶")][bstack11l11l1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ↷")] = bstack111ll11ll1_opy_
            else:
                bstack1lll11l1_opy_[bstack11l11l1_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭↸")] = bstack111ll11ll1_opy_
        if event_url == bstack11l11l1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ↹"):
            cls.bstack1llll11l11ll_opy_()
            logger.debug(bstack11l11l1_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ↺").format(bstack1lll11l1_opy_[bstack11l11l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↻")]))
            cls.bstack11l11l11l1l_opy_.add(bstack1lll11l1_opy_)
        elif event_url == bstack11l11l1_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ↼"):
            cls.post_data([bstack1lll11l1_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l11l11l_opy_(cls, logs):
        for log in logs:
            bstack1llll11l1lll_opy_ = {
                bstack11l11l1_opy_ (u"࠭࡫ࡪࡰࡧࠫ↽"): bstack11l11l1_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩ↾"),
                bstack11l11l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ↿"): log[bstack11l11l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⇀")],
                bstack11l11l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⇁"): log[bstack11l11l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇂")],
                bstack11l11l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬ⇃"): {},
                bstack11l11l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇄"): log[bstack11l11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇅")],
            }
            if bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇆") in log:
                bstack1llll11l1lll_opy_[bstack11l11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇇")] = log[bstack11l11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇈")]
            elif bstack11l11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇉") in log:
                bstack1llll11l1lll_opy_[bstack11l11l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇊")] = log[bstack11l11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇋")]
            cls.bstack1l1ll111_opy_({
                bstack11l11l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇌"): bstack11l11l1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⇍"),
                bstack11l11l1_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ⇎"): [bstack1llll11l1lll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l111l1_opy_(cls, steps):
        bstack1llll1l11lll_opy_ = []
        for step in steps:
            bstack1llll1l11l11_opy_ = {
                bstack11l11l1_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ⇏"): bstack11l11l1_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧ⇐"),
                bstack11l11l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⇑"): step[bstack11l11l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇒")],
                bstack11l11l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇓"): step[bstack11l11l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇔")],
                bstack11l11l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇕"): step[bstack11l11l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⇖")],
                bstack11l11l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⇗"): step[bstack11l11l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⇘")]
            }
            if bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇙") in step:
                bstack1llll1l11l11_opy_[bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇚")] = step[bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇛")]
            elif bstack11l11l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇜") in step:
                bstack1llll1l11l11_opy_[bstack11l11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇝")] = step[bstack11l11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇞")]
            bstack1llll1l11lll_opy_.append(bstack1llll1l11l11_opy_)
        cls.bstack1l1ll111_opy_({
            bstack11l11l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇟"): bstack11l11l1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ⇠"),
            bstack11l11l1_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ⇡"): bstack1llll1l11lll_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack111l111l1l_opy_, stage=STAGE.bstack1ll1lllll_opy_)
    def bstack1lll1ll111_opy_(cls, screenshot):
        cls.bstack1l1ll111_opy_({
            bstack11l11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇢"): bstack11l11l1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⇣"),
            bstack11l11l1_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⇤"): [{
                bstack11l11l1_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⇥"): bstack11l11l1_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧ⇦"),
                bstack11l11l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇧"): datetime.datetime.utcnow().isoformat() + bstack11l11l1_opy_ (u"࡛ࠧࠩ⇨"),
                bstack11l11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇩"): screenshot[bstack11l11l1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ⇪")],
                bstack11l11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇫"): screenshot[bstack11l11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇬")]
            }]
        }, event_url=bstack11l11l1_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇭"))
    @classmethod
    @error_handler(class_method=True)
    def bstack111l1ll111_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l1ll111_opy_({
            bstack11l11l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇮"): bstack11l11l1_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ⇯"),
            bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ⇰"): {
                bstack11l11l1_opy_ (u"ࠤࡸࡹ࡮ࡪࠢ⇱"): cls.current_test_uuid(),
                bstack11l11l1_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤ⇲"): cls.bstack1ll11lll_opy_(driver)
            }
        })
    @classmethod
    def bstack1l1l111l_opy_(cls, event: str, bstack1lll11l1_opy_: bstack1l11ll11_opy_):
        bstack1l11l1l1_opy_ = {
            bstack11l11l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇳"): event,
            bstack1lll11l1_opy_.event_key(): bstack1lll11l1_opy_.bstack11lll11l_opy_(event)
        }
        cls.bstack1l1ll111_opy_(bstack1l11l1l1_opy_)
        result = getattr(bstack1lll11l1_opy_, bstack11l11l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⇴"), None)
        if event == bstack11l11l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⇵"):
            threading.current_thread().bstackTestMeta = {bstack11l11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⇶"): bstack11l11l1_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⇷")}
        elif event == bstack11l11l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⇸"):
            threading.current_thread().bstackTestMeta = {bstack11l11l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ⇹"): getattr(result, bstack11l11l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⇺"), bstack11l11l1_opy_ (u"ࠬ࠭⇻"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ⇼"), None) is None or os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⇽")] == bstack11l11l1_opy_ (u"ࠣࡰࡸࡰࡱࠨ⇾")) and (os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ⇿"), None) is None or os.environ[bstack11l11l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ∀")] == bstack11l11l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ∁")):
            return False
        return True
    @staticmethod
    def bstack1llll1l1l111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11l111_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11l11l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ∂"): bstack11l11l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ∃"),
            bstack11l11l1_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪ∄"): bstack11l11l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭∅")
        }
        if os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭∆"), None):
            headers[bstack11l11l1_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ∇")] = bstack11l11l1_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧ∈").format(os.environ[bstack11l11l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤ∉")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11l11l1_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ∊").format(bstack1llll11ll1l1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11l11l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ∋"), None)
    @staticmethod
    def bstack1ll11lll_opy_(driver):
        return {
            bstack111l11ll11l_opy_(): bstack111l1l11lll_opy_(driver)
        }
    @staticmethod
    def bstack1llll11l1ll1_opy_(exception_info, report):
        return [{bstack11l11l1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ∌"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111111l1ll_opy_(typename):
        if bstack11l11l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ∍") in typename:
            return bstack11l11l1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ∎")
        return bstack11l11l1_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ∏")