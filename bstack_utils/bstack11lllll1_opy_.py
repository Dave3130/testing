# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1111l11_opy_, bstack111l1ll11l1_opy_, bstack1lll111l1l_opy_, error_handler, bstack111l1111111_opy_, bstack111l1ll1lll_opy_, bstack111l1lll11l_opy_, bstack1l1111l1_opy_, bstack1lll111l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l111lllll_opy_ import bstack111ll1111ll_opy_
import bstack_utils.bstack11llll111_opy_ as bstack11l11l11ll_opy_
from bstack_utils.bstack1lll11l1_opy_ import bstack1ll11l11_opy_
import bstack_utils.accessibility as bstack111ll11l_opy_
from bstack_utils.bstack11ll1111l_opy_ import bstack11ll1111l_opy_
from bstack_utils.bstack1l11l111_opy_ import bstack1ll111l1_opy_
from bstack_utils.constants import bstack1ll111111_opy_
bstack1llll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡨࡵ࡬࡭ࡧࡦࡸࡴࡸ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪℙ")
logger = logging.getLogger(__name__)
class bstack1ll1l11l_opy_:
    bstack11l111lllll_opy_ = None
    bs_config = None
    bstack1ll1111ll1_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11llll11_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def launch(cls, bs_config, bstack1ll1111ll1_opy_):
        cls.bs_config = bs_config
        cls.bstack1ll1111ll1_opy_ = bstack1ll1111ll1_opy_
        try:
            cls.bstack1llll1l111l1_opy_()
            bstack1llll1l1llll_opy_ = bstack111l1111l11_opy_(bs_config)
            bstack1llll1lll1l1_opy_ = bstack111l1ll11l1_opy_(bs_config)
            data = bstack11l11l11ll_opy_.bstack1llll11l111l_opy_(bs_config, bstack1ll1111ll1_opy_)
            config = {
                bstack11lll1_opy_ (u"ࠫࡦࡻࡴࡩࠩℚ"): (bstack1llll1l1llll_opy_, bstack1llll1lll1l1_opy_),
                bstack11lll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ℛ"): cls.default_headers()
            }
            response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"࠭ࡐࡐࡕࡗࠫℜ"), cls.request_url(bstack11lll1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠸࠯ࡣࡷ࡬ࡰࡩࡹࠧℝ")), data, config)
            if response.status_code != 200:
                bstack1ll111ll1l_opy_ = response.json()
                if bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ℞")] == False:
                    cls.bstack1llll11l11l1_opy_(bstack1ll111ll1l_opy_)
                    return
                cls.bstack1llll11ll11l_opy_(bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ℟")])
                cls.bstack1llll11lllll_opy_(bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ℠")])
                return None
            bstack1llll11ll1ll_opy_ = cls.bstack1llll11l1ll1_opy_(response)
            return bstack1llll11ll1ll_opy_, response.json()
        except Exception as error:
            logger.error(bstack11lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡧࡱࡵࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࡻࡾࠤ℡").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll11l11ll_opy_=None):
        if not bstack1ll11l11_opy_.on() and not bstack111ll11l_opy_.on():
            return
        if os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ™")) == bstack11lll1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ℣") or os.environ.get(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬℤ")) == bstack11lll1_opy_ (u"ࠣࡰࡸࡰࡱࠨ℥"):
            logger.error(bstack11lll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬΩ"))
            return {
                bstack11lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ℧"): bstack11lll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪℨ"),
                bstack11lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭℩"): bstack11lll1_opy_ (u"࠭ࡔࡰ࡭ࡨࡲ࠴ࡨࡵࡪ࡮ࡧࡍࡉࠦࡩࡴࠢࡸࡲࡩ࡫ࡦࡪࡰࡨࡨ࠱ࠦࡢࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠ࡮࡫ࡪ࡬ࡹࠦࡨࡢࡸࡨࠤ࡫ࡧࡩ࡭ࡧࡧࠫK")
            }
        try:
            cls.bstack11l111lllll_opy_.shutdown()
            data = {
                bstack11lll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬÅ"): bstack1l1111l1_opy_()
            }
            if not bstack1llll11l11ll_opy_ is None:
                data[bstack11lll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡱࡪࡺࡡࡥࡣࡷࡥࠬℬ")] = [{
                    bstack11lll1_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩℭ"): bstack11lll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡠ࡭࡬ࡰࡱ࡫ࡤࠨ℮"),
                    bstack11lll1_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࠫℯ"): bstack1llll11l11ll_opy_
                }]
            config = {
                bstack11lll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ℰ"): cls.default_headers()
            }
            bstack11ll11l11l1_opy_ = bstack11lll1_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡸࡴࡶࠧℱ").format(os.environ[bstack11lll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧℲ")])
            bstack1llll1l11ll1_opy_ = cls.request_url(bstack11ll11l11l1_opy_)
            response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠨࡒࡘࡘࠬℳ"), bstack1llll1l11ll1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11lll1_opy_ (u"ࠤࡖࡸࡴࡶࠠࡳࡧࡴࡹࡪࡹࡴࠡࡰࡲࡸࠥࡵ࡫ࠣℴ"))
        except Exception as error:
            logger.error(bstack11lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾࠿ࠦࠢℵ") + str(error))
            return {
                bstack11lll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫℶ"): bstack11lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫℷ"),
                bstack11lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧℸ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l1ll1_opy_(cls, response):
        bstack1ll111ll1l_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11ll1ll_opy_ = {}
        if bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠧ࡫ࡹࡷࠫℹ")) is None:
            os.environ[bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ℺")] = bstack11lll1_opy_ (u"ࠩࡱࡹࡱࡲࠧ℻")
        else:
            os.environ[bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧℼ")] = bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠫ࡯ࡽࡴࠨℽ"), bstack11lll1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪℾ"))
        os.environ[bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫℿ")] = bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ⅀"), bstack11lll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭⅁"))
        logger.info(bstack11lll1_opy_ (u"ࠩࡗࡩࡸࡺࡨࡶࡤࠣࡷࡹࡧࡲࡵࡧࡧࠤࡼ࡯ࡴࡩࠢ࡬ࡨ࠿ࠦࠧ⅂") + os.getenv(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ⅃")));
        if bstack1ll11l11_opy_.bstack11l11l11l11_opy_(cls.bs_config, cls.bstack1ll1111ll1_opy_.get(bstack11lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬ⅄"), bstack11lll1_opy_ (u"ࠬ࠭ⅅ"))) is True:
            bstack11ll11l11ll_opy_, build_hashed_id, bstack1llll1l11111_opy_ = cls.bstack1llll11llll1_opy_(bstack1ll111ll1l_opy_)
            if bstack11ll11l11ll_opy_ != None and build_hashed_id != None:
                bstack1llll11ll1ll_opy_[bstack11lll1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ⅆ")] = {
                    bstack11lll1_opy_ (u"ࠧ࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠪⅇ"): bstack11ll11l11ll_opy_,
                    bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅈ"): build_hashed_id,
                    bstack11lll1_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ⅉ"): bstack1llll1l11111_opy_
                }
            else:
                bstack1llll11ll1ll_opy_[bstack11lll1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅊")] = {}
        else:
            bstack1llll11ll1ll_opy_[bstack11lll1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⅋")] = {}
        bstack1llll1l11l11_opy_, build_hashed_id = cls.bstack1llll111llll_opy_(bstack1ll111ll1l_opy_)
        if bstack1llll1l11l11_opy_ != None and build_hashed_id != None:
            bstack1llll11ll1ll_opy_[bstack11lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅌")] = {
                bstack11lll1_opy_ (u"࠭ࡡࡶࡶ࡫ࡣࡹࡵ࡫ࡦࡰࠪ⅍"): bstack1llll1l11l11_opy_,
                bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅎ"): build_hashed_id,
            }
        else:
            bstack1llll11ll1ll_opy_[bstack11lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⅏")] = {}
        if bstack1llll11ll1ll_opy_[bstack11lll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅐")].get(bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ⅑")) != None or bstack1llll11ll1ll_opy_[bstack11lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅒")].get(bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ⅓")) != None:
            cls.bstack1llll11ll111_opy_(bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"࠭ࡪࡸࡶࠪ⅔")), bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ⅕")))
        return bstack1llll11ll1ll_opy_
    @classmethod
    def bstack1llll11llll1_opy_(cls, bstack1ll111ll1l_opy_):
        if bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⅖")) == None:
            cls.bstack1llll11ll11l_opy_()
            return [None, None, None]
        if bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")][bstack11lll1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ⅘")] != True:
            cls.bstack1llll11ll11l_opy_(bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⅙")])
            return [None, None, None]
        logger.debug(bstack11lll1_opy_ (u"ࠬࢁࡽࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧ⅚").format(bstack1ll111111_opy_))
        os.environ[bstack11lll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬ⅛")] = bstack11lll1_opy_ (u"ࠧࡵࡴࡸࡩࠬ⅜")
        if bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠨ࡬ࡺࡸࠬ⅝")):
            os.environ[bstack11lll1_opy_ (u"ࠩࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙࡟ࡇࡑࡕࡣࡈࡘࡁࡔࡊࡢࡖࡊࡖࡏࡓࡖࡌࡒࡌ࠭⅞")] = json.dumps({
                bstack11lll1_opy_ (u"ࠪࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ⅟"): bstack111l1111l11_opy_(cls.bs_config),
                bstack11lll1_opy_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭Ⅰ"): bstack111l1ll11l1_opy_(cls.bs_config)
            })
        if bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧⅡ")):
            os.environ[bstack11lll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬⅢ")] = bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅣ")]
        if bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨⅤ")].get(bstack11lll1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪⅥ"), {}).get(bstack11lll1_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧⅦ")):
            os.environ[bstack11lll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬⅧ")] = str(bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅨ")][bstack11lll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧⅩ")][bstack11lll1_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫⅪ")])
        else:
            os.environ[bstack11lll1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩⅫ")] = bstack11lll1_opy_ (u"ࠤࡱࡹࡱࡲࠢⅬ")
        return [bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠪ࡮ࡼࡺࠧⅭ")], bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭Ⅾ")], os.environ[bstack11lll1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭Ⅿ")]]
    @classmethod
    def bstack1llll111llll_opy_(cls, bstack1ll111ll1l_opy_):
        if bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ⅰ")) == None:
            cls.bstack1llll11lllll_opy_()
            return [None, None]
        if bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅱ")][bstack11lll1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩⅲ")] != True:
            cls.bstack1llll11lllll_opy_(bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩⅳ")])
            return [None, None]
        if bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅴ")].get(bstack11lll1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬⅵ")):
            logger.debug(bstack11lll1_opy_ (u"࡚ࠬࡥࡴࡶࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠢࠩⅶ"))
            parsed = json.loads(os.getenv(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧⅷ"), bstack11lll1_opy_ (u"ࠧࡼࡿࠪⅸ")))
            capabilities = bstack11l11l11ll_opy_.bstack1llll11l1lll_opy_(bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅹ")][bstack11lll1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪⅺ")][bstack11lll1_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩⅻ")], bstack11lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩⅼ"), bstack11lll1_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫⅽ"))
            bstack1llll1l11l11_opy_ = capabilities[bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫⅾ")]
            os.environ[bstack11lll1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬⅿ")] = bstack1llll1l11l11_opy_
            if bstack11lll1_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥↀ") in bstack1ll111ll1l_opy_ and bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠤࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠣↁ")) is None:
                parsed[bstack11lll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫↂ")] = capabilities[bstack11lll1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬↃ")]
            os.environ[bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ↄ")] = json.dumps(parsed)
            scripts = bstack11l11l11ll_opy_.bstack1llll11l1lll_opy_(bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ↅ")][bstack11lll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨↆ")][bstack11lll1_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩↇ")], bstack11lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧↈ"), bstack11lll1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࠫ↉"))
            bstack11ll1111l_opy_.bstack11ll111111_opy_(scripts)
            commands = bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ↊")][bstack11lll1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭↋")][bstack11lll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࡕࡱ࡚ࡶࡦࡶࠧ↌")].get(bstack11lll1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ↍"))
            bstack11ll1111l_opy_.bstack1lllll111l11_opy_(commands)
            bstack1lllll11l1l1_opy_ = capabilities.get(bstack11lll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭↎"))
            bstack11ll1111l_opy_.bstack1lllll111l1l_opy_(bstack1lllll11l1l1_opy_)
            bstack11ll1111l_opy_.store()
        return [bstack1llll1l11l11_opy_, bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ↏")]]
    @classmethod
    def bstack1llll11ll11l_opy_(cls, response=None):
        os.environ[bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ←")] = bstack11lll1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ↑")
        os.environ[bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ→")] = bstack11lll1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ↓")
        os.environ[bstack11lll1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭↔")] = bstack11lll1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ↕")
        os.environ[bstack11lll1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨ↖")] = bstack11lll1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ↗")
        os.environ[bstack11lll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ↘")] = bstack11lll1_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ↙")
        cls.bstack1llll11l11l1_opy_(response, bstack11lll1_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨ↚"))
        return [None, None, None]
    @classmethod
    def bstack1llll11lllll_opy_(cls, response=None):
        os.environ[bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ↛")] = bstack11lll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭↜")
        os.environ[bstack11lll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ↝")] = bstack11lll1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ↞")
        os.environ[bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ↟")] = bstack11lll1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ↠")
        cls.bstack1llll11l11l1_opy_(response, bstack11lll1_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠨ↡"))
        return [None, None, None]
    @classmethod
    def bstack1llll11ll111_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ↢")] = jwt
        os.environ[bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭↣")] = build_hashed_id
    @classmethod
    def bstack1llll11l11l1_opy_(cls, response=None, product=bstack11lll1_opy_ (u"ࠤࠥ↤")):
        if response == None or response.get(bstack11lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪ↥")) == None:
            logger.error(product + bstack11lll1_opy_ (u"ࠦࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠨ↦"))
            return
        for error in response[bstack11lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ↧")]:
            bstack111l11ll111_opy_ = error[bstack11lll1_opy_ (u"࠭࡫ࡦࡻࠪ↨")]
            error_message = error[bstack11lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ↩")]
            if error_message:
                if bstack111l11ll111_opy_ == bstack11lll1_opy_ (u"ࠣࡇࡕࡖࡔࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡅࡇࡑࡍࡊࡊࠢ↪"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11lll1_opy_ (u"ࠤࡇࡥࡹࡧࠠࡶࡲ࡯ࡳࡦࡪࠠࡵࡱࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࠥ↫") + product + bstack11lll1_opy_ (u"ࠥࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣ↬"))
    @classmethod
    def bstack1llll1l111l1_opy_(cls):
        if cls.bstack11l111lllll_opy_ is not None:
            return
        cls.bstack11l111lllll_opy_ = bstack111ll1111ll_opy_(cls.post_data)
        cls.bstack11l111lllll_opy_.start()
    @classmethod
    def bstack1ll1111l_opy_(cls):
        if cls.bstack11l111lllll_opy_ is None:
            return
        cls.bstack11l111lllll_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1ll1llll_opy_, event_url=bstack11lll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ↭")):
        config = {
            bstack11lll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭↮"): cls.default_headers()
        }
        logger.debug(bstack11lll1_opy_ (u"ࠨࡰࡰࡵࡷࡣࡩࡧࡴࡢ࠼ࠣࡗࡪࡴࡤࡪࡰࡪࠤࡩࡧࡴࡢࠢࡷࡳࠥࡺࡥࡴࡶ࡫ࡹࡧࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࡵࠣࡿࢂࠨ↯").format(bstack11lll1_opy_ (u"ࠧ࠭ࠢࠪ↰").join([event[bstack11lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↱")] for event in bstack1ll1llll_opy_])))
        response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ↲"), cls.request_url(event_url), bstack1ll1llll_opy_, config)
        bstack1llll1ll1l11_opy_ = response.json()
    @classmethod
    def bstack1lllll11_opy_(cls, bstack1ll1llll_opy_, event_url=bstack11lll1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ↳")):
        logger.debug(bstack11lll1_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡣࡧࡨࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ↴").format(bstack1ll1llll_opy_[bstack11lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↵")]))
        if not bstack11l11l11ll_opy_.bstack1llll1l1111l_opy_(bstack1ll1llll_opy_[bstack11lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↶")]):
            logger.debug(bstack11lll1_opy_ (u"ࠢࡴࡧࡱࡨࡤࡪࡡࡵࡣ࠽ࠤࡓࡵࡴࠡࡣࡧࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ↷").format(bstack1ll1llll_opy_[bstack11lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↸")]))
            return
        bstack111111l11l_opy_ = bstack11l11l11ll_opy_.bstack1llll1l11l1l_opy_(bstack1ll1llll_opy_[bstack11lll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↹")], bstack1ll1llll_opy_.get(bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ↺")))
        if bstack111111l11l_opy_ != None:
            if bstack1ll1llll_opy_.get(bstack11lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭↻")) != None:
                bstack1ll1llll_opy_[bstack11lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ↼")][bstack11lll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ↽")] = bstack111111l11l_opy_
            else:
                bstack1ll1llll_opy_[bstack11lll1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ↾")] = bstack111111l11l_opy_
        if event_url == bstack11lll1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ↿"):
            cls.bstack1llll1l111l1_opy_()
            logger.debug(bstack11lll1_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡁࡥࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ⇀").format(bstack1ll1llll_opy_[bstack11lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇁")]))
            cls.bstack11l111lllll_opy_.add(bstack1ll1llll_opy_)
        elif event_url == bstack11lll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ⇂"):
            cls.post_data([bstack1ll1llll_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1ll1l111_opy_(cls, logs):
        for log in logs:
            bstack1llll11l1l11_opy_ = {
                bstack11lll1_opy_ (u"ࠬࡱࡩ࡯ࡦࠪ⇃"): bstack11lll1_opy_ (u"࠭ࡔࡆࡕࡗࡣࡑࡕࡇࠨ⇄"),
                bstack11lll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⇅"): log[bstack11lll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ⇆")],
                bstack11lll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⇇"): log[bstack11lll1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⇈")],
                bstack11lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡡࡵࡩࡸࡶ࡯࡯ࡵࡨࠫ⇉"): {},
                bstack11lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⇊"): log[bstack11lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇋")],
            }
            if bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇌") in log:
                bstack1llll11l1l11_opy_[bstack11lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇍")] = log[bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇎")]
            elif bstack11lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇏") in log:
                bstack1llll11l1l11_opy_[bstack11lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇐")] = log[bstack11lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇑")]
            cls.bstack1lllll11_opy_({
                bstack11lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇒"): bstack11lll1_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ⇓"),
                bstack11lll1_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭⇔"): [bstack1llll11l1l11_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11ll1l1_opy_(cls, steps):
        bstack1llll11lll11_opy_ = []
        for step in steps:
            bstack1llll11l1111_opy_ = {
                bstack11lll1_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ⇕"): bstack11lll1_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡗࡉࡕ࠭⇖"),
                bstack11lll1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ⇗"): step[bstack11lll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⇘")],
                bstack11lll1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇙"): step[bstack11lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇚")],
                bstack11lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇛"): step[bstack11lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇜")],
                bstack11lll1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ⇝"): step[bstack11lll1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⇞")]
            }
            if bstack11lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇟") in step:
                bstack1llll11l1111_opy_[bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇠")] = step[bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇡")]
            elif bstack11lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇢") in step:
                bstack1llll11l1111_opy_[bstack11lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇣")] = step[bstack11lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇤")]
            bstack1llll11lll11_opy_.append(bstack1llll11l1111_opy_)
        cls.bstack1lllll11_opy_({
            bstack11lll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇥"): bstack11lll1_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ⇦"),
            bstack11lll1_opy_ (u"࠭࡬ࡰࡩࡶࠫ⇧"): bstack1llll11lll11_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1ll1l1ll1l_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def bstack111ll11lll_opy_(cls, screenshot):
        cls.bstack1lllll11_opy_({
            bstack11lll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇨"): bstack11lll1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⇩"),
            bstack11lll1_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ⇪"): [{
                bstack11lll1_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ⇫"): bstack11lll1_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࠭⇬"),
                bstack11lll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ⇭"): datetime.datetime.utcnow().isoformat() + bstack11lll1_opy_ (u"࡚࠭ࠨ⇮"),
                bstack11lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇯"): screenshot[bstack11lll1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ⇰")],
                bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇱"): screenshot[bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇲")]
            }]
        }, event_url=bstack11lll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ⇳"))
    @classmethod
    @error_handler(class_method=True)
    def bstack111llll11l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1lllll11_opy_({
            bstack11lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇴"): bstack11lll1_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ⇵"),
            bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ⇶"): {
                bstack11lll1_opy_ (u"ࠣࡷࡸ࡭ࡩࠨ⇷"): cls.current_test_uuid(),
                bstack11lll1_opy_ (u"ࠤ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠣ⇸"): cls.bstack1l111111_opy_(driver)
            }
        })
    @classmethod
    def bstack11lll11l_opy_(cls, event: str, bstack1ll1llll_opy_: bstack1ll111l1_opy_):
        bstack1lll1l11_opy_ = {
            bstack11lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇹"): event,
            bstack1ll1llll_opy_.event_key(): bstack1ll1llll_opy_.bstack1l1ll111_opy_(event)
        }
        cls.bstack1lllll11_opy_(bstack1lll1l11_opy_)
        result = getattr(bstack1ll1llll_opy_, bstack11lll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⇺"), None)
        if event == bstack11lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⇻"):
            threading.current_thread().bstackTestMeta = {bstack11lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⇼"): bstack11lll1_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ⇽")}
        elif event == bstack11lll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⇾"):
            threading.current_thread().bstackTestMeta = {bstack11lll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⇿"): getattr(result, bstack11lll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ∀"), bstack11lll1_opy_ (u"ࠫࠬ∁"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ∂"), None) is None or os.environ[bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ∃")] == bstack11lll1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ∄")) and (os.environ.get(bstack11lll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭∅"), None) is None or os.environ[bstack11lll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ∆")] == bstack11lll1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ∇")):
            return False
        return True
    @staticmethod
    def bstack1llll11l1l1l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1l11l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11lll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ∈"): bstack11lll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ∉"),
            bstack11lll1_opy_ (u"࠭ࡘ࠮ࡄࡖࡘࡆࡉࡋ࠮ࡖࡈࡗ࡙ࡕࡐࡔࠩ∊"): bstack11lll1_opy_ (u"ࠧࡵࡴࡸࡩࠬ∋")
        }
        if os.environ.get(bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ∌"), None):
            headers[bstack11lll1_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ∍")] = bstack11lll1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭∎").format(os.environ[bstack11lll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠣ∏")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11lll1_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫ∐").format(bstack1llll11lll1l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ∑"), None)
    @staticmethod
    def bstack1l111111_opy_(driver):
        return {
            bstack111l1111111_opy_(): bstack111l1ll1lll_opy_(driver)
        }
    @staticmethod
    def bstack1llll1l111ll_opy_(exception_info, report):
        return [{bstack11lll1_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪ−"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1111111l1l_opy_(typename):
        if bstack11lll1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦ∓") in typename:
            return bstack11lll1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥ∔")
        return bstack11lll1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦ∕")