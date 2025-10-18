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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1111l1ll1l1_opy_, bstack1111l11l1ll_opy_, bstack111l1llll1_opy_, error_handler, bstack111l1ll111l_opy_, bstack1111l11ll11_opy_, bstack1111ll11l11_opy_, bstack11lllll1_opy_, bstack1l1lll11_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l111l1_opy_ import bstack111ll1111ll_opy_
import bstack_utils.bstack1l11ll1l1_opy_ as bstack11ll111ll_opy_
from bstack_utils.bstack11lll1ll_opy_ import bstack1lll1lll_opy_
import bstack_utils.accessibility as bstack1111l11l_opy_
from bstack_utils.bstack111l1ll1l_opy_ import bstack111l1ll1l_opy_
from bstack_utils.bstack1ll1l1l1_opy_ import bstack1l1l11ll_opy_
from bstack_utils.constants import bstack11l111l111_opy_
bstack1llll11l1ll1_opy_ = bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡧࡴࡲ࡬ࡦࡥࡷࡳࡷ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ℟")
logger = logging.getLogger(__name__)
class bstack1lll111l_opy_:
    bstack11l11l111l1_opy_ = None
    bs_config = None
    bstack1lllll1lll_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11l1lll1_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def launch(cls, bs_config, bstack1lllll1lll_opy_):
        cls.bs_config = bs_config
        cls.bstack1lllll1lll_opy_ = bstack1lllll1lll_opy_
        try:
            cls.bstack1llll1l111ll_opy_()
            bstack1lllll1111l1_opy_ = bstack1111l1ll1l1_opy_(bs_config)
            bstack1llll1lll1l1_opy_ = bstack1111l11l1ll_opy_(bs_config)
            data = bstack11ll111ll_opy_.bstack1llll11ll111_opy_(bs_config, bstack1lllll1lll_opy_)
            config = {
                bstack11l111_opy_ (u"ࠪࡥࡺࡺࡨࠨ℠"): (bstack1lllll1111l1_opy_, bstack1llll1lll1l1_opy_),
                bstack11l111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ℡"): cls.default_headers()
            }
            response = bstack111l1llll1_opy_(bstack11l111_opy_ (u"ࠬࡖࡏࡔࡖࠪ™"), cls.request_url(bstack11l111_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠷࠵ࡢࡶ࡫࡯ࡨࡸ࠭℣")), data, config)
            if response.status_code != 200:
                bstack1l11lll1l1_opy_ = response.json()
                if bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨℤ")] == False:
                    cls.bstack1llll11l11l1_opy_(bstack1l11lll1l1_opy_)
                    return
                cls.bstack1llll1l11lll_opy_(bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ℥")])
                cls.bstack1llll11l1l11_opy_(bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩΩ")])
                return None
            bstack1llll11lll11_opy_ = cls.bstack1llll11l1lll_opy_(response)
            return bstack1llll11lll11_opy_, response.json()
        except Exception as error:
            logger.error(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࢁࡽࠣ℧").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l11111_opy_=None):
        if not bstack1lll1lll_opy_.on() and not bstack1111l11l_opy_.on():
            return
        if os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨℨ")) == bstack11l111_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ℩") or os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫK")) == bstack11l111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧÅ"):
            logger.error(bstack11l111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡴࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫℬ"))
            return {
                bstack11l111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩℭ"): bstack11l111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ℮"),
                bstack11l111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬℯ"): bstack11l111_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪℰ")
            }
        try:
            cls.bstack11l11l111l1_opy_.shutdown()
            data = {
                bstack11l111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫℱ"): bstack11lllll1_opy_()
            }
            if not bstack1llll1l11111_opy_ is None:
                data[bstack11l111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡰࡩࡹࡧࡤࡢࡶࡤࠫℲ")] = [{
                    bstack11l111_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨℳ"): bstack11l111_opy_ (u"ࠩࡸࡷࡪࡸ࡟࡬࡫࡯ࡰࡪࡪࠧℴ"),
                    bstack11l111_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࠪℵ"): bstack1llll1l11111_opy_
                }]
            config = {
                bstack11l111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬℶ"): cls.default_headers()
            }
            bstack11ll111ll11_opy_ = bstack11l111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡷࡳࡵ࠭ℷ").format(os.environ[bstack11l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦℸ")])
            bstack1llll11ll1ll_opy_ = cls.request_url(bstack11ll111ll11_opy_)
            response = bstack111l1llll1_opy_(bstack11l111_opy_ (u"ࠧࡑࡗࡗࠫℹ"), bstack1llll11ll1ll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11l111_opy_ (u"ࠣࡕࡷࡳࡵࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡯ࡱࡷࠤࡴࡱࠢ℺"))
        except Exception as error:
            logger.error(bstack11l111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽࠾ࠥࠨ℻") + str(error))
            return {
                bstack11l111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪℼ"): bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪℽ"),
                bstack11l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ℾ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l1lll_opy_(cls, response):
        bstack1l11lll1l1_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11lll11_opy_ = {}
        if bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"࠭ࡪࡸࡶࠪℿ")) is None:
            os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⅀")] = bstack11l111_opy_ (u"ࠨࡰࡸࡰࡱ࠭⅁")
        else:
            os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⅂")] = bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"ࠪ࡮ࡼࡺࠧ⅃"), bstack11l111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ⅄"))
        os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪⅅ")] = bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅆ"), bstack11l111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅇ"))
        logger.info(bstack11l111_opy_ (u"ࠨࡖࡨࡷࡹ࡮ࡵࡣࠢࡶࡸࡦࡸࡴࡦࡦࠣࡻ࡮ࡺࡨࠡ࡫ࡧ࠾ࠥ࠭ⅈ") + os.getenv(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧⅉ")));
        if bstack1lll1lll_opy_.bstack11l11l11l11_opy_(cls.bs_config, cls.bstack1lllll1lll_opy_.get(bstack11l111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫ⅊"), bstack11l111_opy_ (u"ࠫࠬ⅋"))) is True:
            bstack11ll11l1111_opy_, build_hashed_id, bstack1llll1l11l11_opy_ = cls.bstack1llll1l11l1l_opy_(bstack1l11lll1l1_opy_)
            if bstack11ll11l1111_opy_ != None and build_hashed_id != None:
                bstack1llll11lll11_opy_[bstack11l111_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅌")] = {
                    bstack11l111_opy_ (u"࠭ࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠩ⅍"): bstack11ll11l1111_opy_,
                    bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅎ"): build_hashed_id,
                    bstack11l111_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬ⅏"): bstack1llll1l11l11_opy_
                }
            else:
                bstack1llll11lll11_opy_[bstack11l111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅐")] = {}
        else:
            bstack1llll11lll11_opy_[bstack11l111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅑")] = {}
        bstack1llll11l111l_opy_, build_hashed_id = cls.bstack1llll11l11ll_opy_(bstack1l11lll1l1_opy_)
        if bstack1llll11l111l_opy_ != None and build_hashed_id != None:
            bstack1llll11lll11_opy_[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅒")] = {
                bstack11l111_opy_ (u"ࠬࡧࡵࡵࡪࡢࡸࡴࡱࡥ࡯ࠩ⅓"): bstack1llll11l111l_opy_,
                bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⅔"): build_hashed_id,
            }
        else:
            bstack1llll11lll11_opy_[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⅕")] = {}
        if bstack1llll11lll11_opy_[bstack11l111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⅖")].get(bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⅗")) != None or bstack1llll11lll11_opy_[bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⅘")].get(bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅙")) != None:
            cls.bstack1llll11ll11l_opy_(bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"ࠬࡰࡷࡵࠩ⅚")), bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⅛")))
        return bstack1llll11lll11_opy_
    @classmethod
    def bstack1llll1l11l1l_opy_(cls, bstack1l11lll1l1_opy_):
        if bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ⅜")) == None:
            cls.bstack1llll1l11lll_opy_()
            return [None, None, None]
        if bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⅝")][bstack11l111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ⅞")] != True:
            cls.bstack1llll1l11lll_opy_(bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅟")])
            return [None, None, None]
        logger.debug(bstack11l111_opy_ (u"ࠫࢀࢃࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭Ⅰ").format(bstack11l111l111_opy_))
        os.environ[bstack11l111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫⅡ")] = bstack11l111_opy_ (u"࠭ࡴࡳࡷࡨࠫⅢ")
        if bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"ࠧ࡫ࡹࡷࠫⅣ")):
            os.environ[bstack11l111_opy_ (u"ࠨࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘࡥࡆࡐࡔࡢࡇࡗࡇࡓࡉࡡࡕࡉࡕࡕࡒࡕࡋࡑࡋࠬⅤ")] = json.dumps({
                bstack11l111_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫⅥ"): bstack1111l1ll1l1_opy_(cls.bs_config),
                bstack11l111_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬⅦ"): bstack1111l11l1ll_opy_(cls.bs_config)
            })
        if bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭Ⅷ")):
            os.environ[bstack11l111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫⅨ")] = bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅩ")]
        if bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅪ")].get(bstack11l111_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩⅫ"), {}).get(bstack11l111_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭Ⅼ")):
            os.environ[bstack11l111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫⅭ")] = str(bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫⅮ")][bstack11l111_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭Ⅿ")][bstack11l111_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪⅰ")])
        else:
            os.environ[bstack11l111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨⅱ")] = bstack11l111_opy_ (u"ࠣࡰࡸࡰࡱࠨⅲ")
        return [bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠩ࡭ࡻࡹ࠭ⅳ")], bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬⅴ")], os.environ[bstack11l111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬⅵ")]]
    @classmethod
    def bstack1llll11l11ll_opy_(cls, bstack1l11lll1l1_opy_):
        if bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬⅶ")) == None:
            cls.bstack1llll11l1l11_opy_()
            return [None, None]
        if bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ⅷ")][bstack11l111_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨⅸ")] != True:
            cls.bstack1llll11l1l11_opy_(bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅹ")])
            return [None, None]
        if bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩⅺ")].get(bstack11l111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫⅻ")):
            logger.debug(bstack11l111_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨⅼ"))
            parsed = json.loads(os.getenv(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ⅽ"), bstack11l111_opy_ (u"࠭ࡻࡾࠩⅾ")))
            capabilities = bstack11ll111ll_opy_.bstack1llll1l1111l_opy_(bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅿ")][bstack11l111_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩↀ")][bstack11l111_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨↁ")], bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨↂ"), bstack11l111_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪↃ"))
            bstack1llll11l111l_opy_ = capabilities[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪↄ")]
            os.environ[bstack11l111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫↅ")] = bstack1llll11l111l_opy_
            if bstack11l111_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤↆ") in bstack1l11lll1l1_opy_ and bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"ࠣࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠢↇ")) is None:
                parsed[bstack11l111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪↈ")] = capabilities[bstack11l111_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ↉")]
            os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ↊")] = json.dumps(parsed)
            scripts = bstack11ll111ll_opy_.bstack1llll1l1111l_opy_(bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ↋")][bstack11l111_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ↌")][bstack11l111_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ↍")], bstack11l111_opy_ (u"ࠨࡰࡤࡱࡪ࠭↎"), bstack11l111_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࠪ↏"))
            bstack111l1ll1l_opy_.bstack1l1l1lll1_opy_(scripts)
            commands = bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ←")][bstack11l111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ↑")][bstack11l111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࡔࡰ࡙ࡵࡥࡵ࠭→")].get(bstack11l111_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ↓"))
            bstack111l1ll1l_opy_.bstack1lllll11l11l_opy_(commands)
            bstack1lllll11l1ll_opy_ = capabilities.get(bstack11l111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ↔"))
            bstack111l1ll1l_opy_.bstack1lllll11l1l1_opy_(bstack1lllll11l1ll_opy_)
            bstack111l1ll1l_opy_.store()
        return [bstack1llll11l111l_opy_, bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ↕")]]
    @classmethod
    def bstack1llll1l11lll_opy_(cls, response=None):
        os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ↖")] = bstack11l111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ↗")
        os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ↘")] = bstack11l111_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ↙")
        os.environ[bstack11l111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬ↚")] = bstack11l111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭↛")
        os.environ[bstack11l111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧ↜")] = bstack11l111_opy_ (u"ࠤࡱࡹࡱࡲࠢ↝")
        os.environ[bstack11l111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ↞")] = bstack11l111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ↟")
        cls.bstack1llll11l11l1_opy_(response, bstack11l111_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧ↠"))
        return [None, None, None]
    @classmethod
    def bstack1llll11l1l11_opy_(cls, response=None):
        os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ↡")] = bstack11l111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ↢")
        os.environ[bstack11l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭↣")] = bstack11l111_opy_ (u"ࠩࡱࡹࡱࡲࠧ↤")
        os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ↥")] = bstack11l111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ↦")
        cls.bstack1llll11l11l1_opy_(response, bstack11l111_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧ↧"))
        return [None, None, None]
    @classmethod
    def bstack1llll11ll11l_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ↨")] = jwt
        os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ↩")] = build_hashed_id
    @classmethod
    def bstack1llll11l11l1_opy_(cls, response=None, product=bstack11l111_opy_ (u"ࠣࠤ↪")):
        if response == None or response.get(bstack11l111_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ↫")) == None:
            logger.error(product + bstack11l111_opy_ (u"ࠥࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠧ↬"))
            return
        for error in response[bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ↭")]:
            bstack1111llll111_opy_ = error[bstack11l111_opy_ (u"ࠬࡱࡥࡺࠩ↮")]
            error_message = error[bstack11l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ↯")]
            if error_message:
                if bstack1111llll111_opy_ == bstack11l111_opy_ (u"ࠢࡆࡔࡕࡓࡗࡥࡁࡄࡅࡈࡗࡘࡥࡄࡆࡐࡌࡉࡉࠨ↰"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11l111_opy_ (u"ࠣࡆࡤࡸࡦࠦࡵࡱ࡮ࡲࡥࡩࠦࡴࡰࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࠤ↱") + product + bstack11l111_opy_ (u"ࠤࠣࡪࡦ࡯࡬ࡦࡦࠣࡨࡺ࡫ࠠࡵࡱࠣࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢ↲"))
    @classmethod
    def bstack1llll1l111ll_opy_(cls):
        if cls.bstack11l11l111l1_opy_ is not None:
            return
        cls.bstack11l11l111l1_opy_ = bstack111ll1111ll_opy_(cls.post_data)
        cls.bstack11l11l111l1_opy_.start()
    @classmethod
    def bstack1ll1l1ll_opy_(cls):
        if cls.bstack11l11l111l1_opy_ is None:
            return
        cls.bstack11l11l111l1_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l11l111_opy_, event_url=bstack11l111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ↳")):
        config = {
            bstack11l111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ↴"): cls.default_headers()
        }
        logger.debug(bstack11l111_opy_ (u"ࠧࡶ࡯ࡴࡶࡢࡨࡦࡺࡡ࠻ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡶࡲࠤࡹ࡫ࡳࡵࡪࡸࡦࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡴࠢࡾࢁࠧ↵").format(bstack11l111_opy_ (u"࠭ࠬࠡࠩ↶").join([event[bstack11l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↷")] for event in bstack1l11l111_opy_])))
        response = bstack111l1llll1_opy_(bstack11l111_opy_ (u"ࠨࡒࡒࡗ࡙࠭↸"), cls.request_url(event_url), bstack1l11l111_opy_, config)
        bstack1llll1lll1ll_opy_ = response.json()
    @classmethod
    def bstack1ll11lll_opy_(cls, bstack1l11l111_opy_, event_url=bstack11l111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ↹")):
        logger.debug(bstack11l111_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡢࡦࡧࠤࡩࡧࡴࡢࠢࡷࡳࠥࡨࡡࡵࡥ࡫ࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ↺").format(bstack1l11l111_opy_[bstack11l111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↻")]))
        if not bstack11ll111ll_opy_.bstack1llll11ll1l1_opy_(bstack1l11l111_opy_[bstack11l111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↼")]):
            logger.debug(bstack11l111_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡒࡴࡺࠠࡢࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ↽").format(bstack1l11l111_opy_[bstack11l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↾")]))
            return
        bstack111ll111l1_opy_ = bstack11ll111ll_opy_.bstack1llll1l11ll1_opy_(bstack1l11l111_opy_[bstack11l111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↿")], bstack1l11l111_opy_.get(bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⇀")))
        if bstack111ll111l1_opy_ != None:
            if bstack1l11l111_opy_.get(bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ⇁")) != None:
                bstack1l11l111_opy_[bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⇂")][bstack11l111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ⇃")] = bstack111ll111l1_opy_
            else:
                bstack1l11l111_opy_[bstack11l111_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ⇄")] = bstack111ll111l1_opy_
        if event_url == bstack11l111_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭⇅"):
            cls.bstack1llll1l111ll_opy_()
            logger.debug(bstack11l111_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡇࡤࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ⇆").format(bstack1l11l111_opy_[bstack11l111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇇")]))
            cls.bstack11l11l111l1_opy_.add(bstack1l11l111_opy_)
        elif event_url == bstack11l111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⇈"):
            cls.post_data([bstack1l11l111_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1ll1l111_opy_(cls, logs):
        for log in logs:
            bstack1llll11lll1l_opy_ = {
                bstack11l111_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⇉"): bstack11l111_opy_ (u"࡚ࠬࡅࡔࡖࡢࡐࡔࡍࠧ⇊"),
                bstack11l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇋"): log[bstack11l111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⇌")],
                bstack11l111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇍"): log[bstack11l111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⇎")],
                bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࠪ⇏"): {},
                bstack11l111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⇐"): log[bstack11l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⇑")],
            }
            if bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇒") in log:
                bstack1llll11lll1l_opy_[bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇓")] = log[bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇔")]
            elif bstack11l111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇕") in log:
                bstack1llll11lll1l_opy_[bstack11l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇖")] = log[bstack11l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇗")]
            cls.bstack1ll11lll_opy_({
                bstack11l111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇘"): bstack11l111_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ⇙"),
                bstack11l111_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ⇚"): [bstack1llll11lll1l_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11llll1_opy_(cls, steps):
        bstack1llll11l1l1l_opy_ = []
        for step in steps:
            bstack1llll11lllll_opy_ = {
                bstack11l111_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭⇛"): bstack11l111_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡖࡈࡔࠬ⇜"),
                bstack11l111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ⇝"): step[bstack11l111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ⇞")],
                bstack11l111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ⇟"): step[bstack11l111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇠")],
                bstack11l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇡"): step[bstack11l111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇢")],
                bstack11l111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ⇣"): step[bstack11l111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ⇤")]
            }
            if bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇥") in step:
                bstack1llll11lllll_opy_[bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇦")] = step[bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇧")]
            elif bstack11l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇨") in step:
                bstack1llll11lllll_opy_[bstack11l111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇩")] = step[bstack11l111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇪")]
            bstack1llll11l1l1l_opy_.append(bstack1llll11lllll_opy_)
        cls.bstack1ll11lll_opy_({
            bstack11l111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇫"): bstack11l111_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ⇬"),
            bstack11l111_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ⇭"): bstack1llll11l1l1l_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1111ll11l1_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack111l11lll_opy_(cls, screenshot):
        cls.bstack1ll11lll_opy_({
            bstack11l111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇮"): bstack11l111_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ⇯"),
            bstack11l111_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭⇰"): [{
                bstack11l111_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ⇱"): bstack11l111_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠬ⇲"),
                bstack11l111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇳"): datetime.datetime.utcnow().isoformat() + bstack11l111_opy_ (u"ࠬࡠࠧ⇴"),
                bstack11l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇵"): screenshot[bstack11l111_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭⇶")],
                bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇷"): screenshot[bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇸")]
            }]
        }, event_url=bstack11l111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⇹"))
    @classmethod
    @error_handler(class_method=True)
    def bstack11l1l1l11_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1ll11lll_opy_({
            bstack11l111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇺"): bstack11l111_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ⇻"),
            bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ⇼"): {
                bstack11l111_opy_ (u"ࠢࡶࡷ࡬ࡨࠧ⇽"): cls.current_test_uuid(),
                bstack11l111_opy_ (u"ࠣ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠢ⇾"): cls.bstack1ll1l11l_opy_(driver)
            }
        })
    @classmethod
    def bstack1l1111l1_opy_(cls, event: str, bstack1l11l111_opy_: bstack1l1l11ll_opy_):
        bstack1ll1111l_opy_ = {
            bstack11l111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇿"): event,
            bstack1l11l111_opy_.event_key(): bstack1l11l111_opy_.bstack1l11llll_opy_(event)
        }
        cls.bstack1ll11lll_opy_(bstack1ll1111l_opy_)
        result = getattr(bstack1l11l111_opy_, bstack11l111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ∀"), None)
        if event == bstack11l111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ∁"):
            threading.current_thread().bstackTestMeta = {bstack11l111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ∂"): bstack11l111_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ∃")}
        elif event == bstack11l111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ∄"):
            threading.current_thread().bstackTestMeta = {bstack11l111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ∅"): getattr(result, bstack11l111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ∆"), bstack11l111_opy_ (u"ࠪࠫ∇"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ∈"), None) is None or os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ∉")] == bstack11l111_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ∊")) and (os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ∋"), None) is None or os.environ[bstack11l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭∌")] == bstack11l111_opy_ (u"ࠤࡱࡹࡱࡲࠢ∍")):
            return False
        return True
    @staticmethod
    def bstack1llll1l111l1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1lll111l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11l111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ∎"): bstack11l111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ∏"),
            bstack11l111_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨ∐"): bstack11l111_opy_ (u"࠭ࡴࡳࡷࡨࠫ∑")
        }
        if os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ−"), None):
            headers[bstack11l111_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ∓")] = bstack11l111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ∔").format(os.environ[bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠢ∕")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11l111_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ∖").format(bstack1llll11l1ll1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ∗"), None)
    @staticmethod
    def bstack1ll1l11l_opy_(driver):
        return {
            bstack111l1ll111l_opy_(): bstack1111l11ll11_opy_(driver)
        }
    @staticmethod
    def bstack1llll11l1111_opy_(exception_info, report):
        return [{bstack11l111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ∘"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1111111lll_opy_(typename):
        if bstack11l111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ∙") in typename:
            return bstack11l111_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤ√")
        return bstack11l111_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥ∛")