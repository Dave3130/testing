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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1l1l111_opy_, bstack1111l1l111l_opy_, bstack1ll1l1lll_opy_, error_handler, bstack1111lll11l1_opy_, bstack1111l1lll11_opy_, bstack1111l1l1111_opy_, bstack1lll1111_opy_, bstack1l1l11l1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l11l11_opy_ import bstack111ll11111l_opy_
import bstack_utils.bstack11l1lll1ll_opy_ as bstack1111l1l11l_opy_
from bstack_utils.bstack1l1ll1l1_opy_ import bstack1l1l111l_opy_
import bstack_utils.accessibility as bstack1111ll11_opy_
from bstack_utils.bstack1l1l1l1l1_opy_ import bstack1l1l1l1l1_opy_
from bstack_utils.bstack1l11ll1l_opy_ import bstack1llll11l_opy_
from bstack_utils.constants import bstack1ll1l1ll11_opy_
bstack1llll11ll11l_opy_ = bstack11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡩ࡯࡭࡮ࡨࡧࡹࡵࡲ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ℡")
logger = logging.getLogger(__name__)
class bstack1l111l1l_opy_:
    bstack11l11l11l11_opy_ = None
    bs_config = None
    bstack1l1l111l1l_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11ll1l1l_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def launch(cls, bs_config, bstack1l1l111l1l_opy_):
        cls.bs_config = bs_config
        cls.bstack1l1l111l1l_opy_ = bstack1l1l111l1l_opy_
        try:
            cls.bstack1llll11l111l_opy_()
            bstack1llll1ll11l1_opy_ = bstack111l1l1l111_opy_(bs_config)
            bstack1llll1ll1lll_opy_ = bstack1111l1l111l_opy_(bs_config)
            data = bstack1111l1l11l_opy_.bstack1llll11l11l1_opy_(bs_config, bstack1l1l111l1l_opy_)
            config = {
                bstack11ll_opy_ (u"ࠬࡧࡵࡵࡪࠪ™"): (bstack1llll1ll11l1_opy_, bstack1llll1ll1lll_opy_),
                bstack11ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ℣"): cls.default_headers()
            }
            response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠧࡑࡑࡖࡘࠬℤ"), cls.request_url(bstack11ll_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠲࠰ࡤࡸ࡭ࡱࡪࡳࠨ℥")), data, config)
            if response.status_code != 200:
                bstack11lll1l11l_opy_ = response.json()
                if bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪΩ")] == False:
                    cls.bstack1llll11ll1ll_opy_(bstack11lll1l11l_opy_)
                    return
                cls.bstack1llll11l1l11_opy_(bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ℧")])
                cls.bstack1llll1l11ll1_opy_(bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℨ")])
                return None
            bstack1llll1l1111l_opy_ = cls.bstack1llll11l1lll_opy_(response)
            return bstack1llll1l1111l_opy_, response.json()
        except Exception as error:
            logger.error(bstack11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡼࡿࠥ℩").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l11l1l_opy_=None):
        if not bstack1l1l111l_opy_.on() and not bstack1111ll11_opy_.on():
            return
        if os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪK")) == bstack11ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧÅ") or os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ℬ")) == bstack11ll_opy_ (u"ࠤࡱࡹࡱࡲࠢℭ"):
            logger.error(bstack11ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭℮"))
            return {
                bstack11ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫℯ"): bstack11ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫℰ"),
                bstack11ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧℱ"): bstack11ll_opy_ (u"ࠧࡕࡱ࡮ࡩࡳ࠵ࡢࡶ࡫࡯ࡨࡎࡊࠠࡪࡵࠣࡹࡳࡪࡥࡧ࡫ࡱࡩࡩ࠲ࠠࡣࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡ࡯࡬࡫࡭ࡺࠠࡩࡣࡹࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠬℲ")
            }
        try:
            cls.bstack11l11l11l11_opy_.shutdown()
            data = {
                bstack11ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ℳ"): bstack1lll1111_opy_()
            }
            if not bstack1llll1l11l1l_opy_ is None:
                data[bstack11ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡲ࡫ࡴࡢࡦࡤࡸࡦ࠭ℴ")] = [{
                    bstack11ll_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪℵ"): bstack11ll_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩℶ"),
                    bstack11ll_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬℷ"): bstack1llll1l11l1l_opy_
                }]
            config = {
                bstack11ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧℸ"): cls.default_headers()
            }
            bstack11ll111l11l_opy_ = bstack11ll_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨℹ").format(os.environ[bstack11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ℺")])
            bstack1llll11ll111_opy_ = cls.request_url(bstack11ll111l11l_opy_)
            response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠩࡓ࡙࡙࠭℻"), bstack1llll11ll111_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11ll_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤℼ"))
        except Exception as error:
            logger.error(bstack11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࡀࠠࠣℽ") + str(error))
            return {
                bstack11ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬℾ"): bstack11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬℿ"),
                bstack11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⅀"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l1lll_opy_(cls, response):
        bstack11lll1l11l_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l1111l_opy_ = {}
        if bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠨ࡬ࡺࡸࠬ⅁")) is None:
            os.environ[bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⅂")] = bstack11ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ⅃")
        else:
            os.environ[bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⅄")] = bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠬࡰࡷࡵࠩⅅ"), bstack11ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫⅆ"))
        os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬⅇ")] = bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅈ"), bstack11ll_opy_ (u"ࠩࡱࡹࡱࡲࠧⅉ"))
        logger.info(bstack11ll_opy_ (u"ࠪࡘࡪࡹࡴࡩࡷࡥࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࠨ⅊") + os.getenv(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ⅋")));
        if bstack1l1l111l_opy_.bstack11l11l11111_opy_(cls.bs_config, cls.bstack1l1l111l1l_opy_.get(bstack11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭⅌"), bstack11ll_opy_ (u"࠭ࠧ⅍"))) is True:
            bstack11ll111llll_opy_, build_hashed_id, bstack1llll1l111l1_opy_ = cls.bstack1llll1l11111_opy_(bstack11lll1l11l_opy_)
            if bstack11ll111llll_opy_ != None and build_hashed_id != None:
                bstack1llll1l1111l_opy_[bstack11ll_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅎ")] = {
                    bstack11ll_opy_ (u"ࠨ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠫ⅏"): bstack11ll111llll_opy_,
                    bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⅐"): build_hashed_id,
                    bstack11ll_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ⅑"): bstack1llll1l111l1_opy_
                }
            else:
                bstack1llll1l1111l_opy_[bstack11ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⅒")] = {}
        else:
            bstack1llll1l1111l_opy_[bstack11ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅓")] = {}
        bstack1llll11l1l1l_opy_, build_hashed_id = cls.bstack1llll11llll1_opy_(bstack11lll1l11l_opy_)
        if bstack1llll11l1l1l_opy_ != None and build_hashed_id != None:
            bstack1llll1l1111l_opy_[bstack11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅔")] = {
                bstack11ll_opy_ (u"ࠧࡢࡷࡷ࡬ࡤࡺ࡯࡬ࡧࡱࠫ⅕"): bstack1llll11l1l1l_opy_,
                bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅖"): build_hashed_id,
            }
        else:
            bstack1llll1l1111l_opy_[bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")] = {}
        if bstack1llll1l1111l_opy_[bstack11ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅘")].get(bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅙")) != None or bstack1llll1l1111l_opy_[bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅚")].get(bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⅛")) != None:
            cls.bstack1llll11l1111_opy_(bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠧ࡫ࡹࡷࠫ⅜")), bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅝")))
        return bstack1llll1l1111l_opy_
    @classmethod
    def bstack1llll1l11111_opy_(cls, bstack11lll1l11l_opy_):
        if bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅞")) == None:
            cls.bstack1llll11l1l11_opy_()
            return [None, None, None]
        if bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅟")][bstack11ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬⅠ")] != True:
            cls.bstack1llll11l1l11_opy_(bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅡ")])
            return [None, None, None]
        logger.debug(bstack11ll_opy_ (u"࠭ࡻࡾࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨⅢ").format(bstack1ll1l1ll11_opy_))
        os.environ[bstack11ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭Ⅳ")] = bstack11ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭Ⅴ")
        if bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠩ࡭ࡻࡹ࠭Ⅵ")):
            os.environ[bstack11ll_opy_ (u"ࠪࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࡠࡈࡒࡖࡤࡉࡒࡂࡕࡋࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧⅦ")] = json.dumps({
                bstack11ll_opy_ (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪ࠭Ⅷ"): bstack111l1l1l111_opy_(cls.bs_config),
                bstack11ll_opy_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧⅨ"): bstack1111l1l111l_opy_(cls.bs_config)
            })
        if bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅩ")):
            os.environ[bstack11ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭Ⅺ")] = bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅫ")]
        if bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩⅬ")].get(bstack11ll_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫⅭ"), {}).get(bstack11ll_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨⅮ")):
            os.environ[bstack11ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭Ⅿ")] = str(bstack11lll1l11l_opy_[bstack11ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ⅰ")][bstack11ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅱ")][bstack11ll_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬⅲ")])
        else:
            os.environ[bstack11ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪⅳ")] = bstack11ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣⅴ")
        return [bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠫ࡯ࡽࡴࠨⅵ")], bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧⅶ")], os.environ[bstack11ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧⅷ")]]
    @classmethod
    def bstack1llll11llll1_opy_(cls, bstack11lll1l11l_opy_):
        if bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅸ")) == None:
            cls.bstack1llll1l11ll1_opy_()
            return [None, None]
        if bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅹ")][bstack11ll_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪⅺ")] != True:
            cls.bstack1llll1l11ll1_opy_(bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅻ")])
            return [None, None]
        if bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫⅼ")].get(bstack11ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ⅽ")):
            logger.debug(bstack11ll_opy_ (u"࠭ࡔࡦࡵࡷࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪⅾ"))
            parsed = json.loads(os.getenv(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨⅿ"), bstack11ll_opy_ (u"ࠨࡽࢀࠫↀ")))
            capabilities = bstack1111l1l11l_opy_.bstack1llll11lll1l_opy_(bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩↁ")][bstack11ll_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫↂ")][bstack11ll_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪↃ")], bstack11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪↄ"), bstack11ll_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬↅ"))
            bstack1llll11l1l1l_opy_ = capabilities[bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬↆ")]
            os.environ[bstack11ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ↇ")] = bstack1llll11l1l1l_opy_
            if bstack11ll_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦↈ") in bstack11lll1l11l_opy_ and bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤ↉")) is None:
                parsed[bstack11ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ↊")] = capabilities[bstack11ll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭↋")]
            os.environ[bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ↌")] = json.dumps(parsed)
            scripts = bstack1111l1l11l_opy_.bstack1llll11lll1l_opy_(bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ↍")][bstack11ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ↎")][bstack11ll_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ↏")], bstack11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ←"), bstack11ll_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࠬ↑"))
            bstack1l1l1l1l1_opy_.bstack1l11l11l1_opy_(scripts)
            commands = bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ→")][bstack11ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ↓")][bstack11ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠨ↔")].get(bstack11ll_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ↕"))
            bstack1l1l1l1l1_opy_.bstack1lllll111lll_opy_(commands)
            bstack1lllll11l111_opy_ = capabilities.get(bstack11ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ↖"))
            bstack1l1l1l1l1_opy_.bstack1lllll111ll1_opy_(bstack1lllll11l111_opy_)
            bstack1l1l1l1l1_opy_.store()
        return [bstack1llll11l1l1l_opy_, bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ↗")]]
    @classmethod
    def bstack1llll11l1l11_opy_(cls, response=None):
        os.environ[bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ↘")] = bstack11ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ↙")
        os.environ[bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ↚")] = bstack11ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ↛")
        os.environ[bstack11ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧ↜")] = bstack11ll_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ↝")
        os.environ[bstack11ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ↞")] = bstack11ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ↟")
        os.environ[bstack11ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭↠")] = bstack11ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ↡")
        cls.bstack1llll11ll1ll_opy_(response, bstack11ll_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢ↢"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l11ll1_opy_(cls, response=None):
        os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭↣")] = bstack11ll_opy_ (u"ࠩࡱࡹࡱࡲࠧ↤")
        os.environ[bstack11ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ↥")] = bstack11ll_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ↦")
        os.environ[bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ↧")] = bstack11ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ↨")
        cls.bstack1llll11ll1ll_opy_(response, bstack11ll_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢ↩"))
        return [None, None, None]
    @classmethod
    def bstack1llll11l1111_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ↪")] = jwt
        os.environ[bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ↫")] = build_hashed_id
    @classmethod
    def bstack1llll11ll1ll_opy_(cls, response=None, product=bstack11ll_opy_ (u"ࠥࠦ↬")):
        if response == None or response.get(bstack11ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ↭")) == None:
            logger.error(product + bstack11ll_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢ↮"))
            return
        for error in response[bstack11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭↯")]:
            bstack1111ll1lll1_opy_ = error[bstack11ll_opy_ (u"ࠧ࡬ࡧࡼࠫ↰")]
            error_message = error[bstack11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↱")]
            if error_message:
                if bstack1111ll1lll1_opy_ == bstack11ll_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣ↲"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11ll_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦ↳") + product + bstack11ll_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤ↴"))
    @classmethod
    def bstack1llll11l111l_opy_(cls):
        if cls.bstack11l11l11l11_opy_ is not None:
            return
        cls.bstack11l11l11l11_opy_ = bstack111ll11111l_opy_(cls.post_data)
        cls.bstack11l11l11l11_opy_.start()
    @classmethod
    def bstack1l1l1111_opy_(cls):
        if cls.bstack11l11l11l11_opy_ is None:
            return
        cls.bstack11l11l11l11_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1ll11l1l_opy_, event_url=bstack11ll_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ↵")):
        config = {
            bstack11ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ↶"): cls.default_headers()
        }
        logger.debug(bstack11ll_opy_ (u"ࠢࡱࡱࡶࡸࡤࡪࡡࡵࡣ࠽ࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡶࠤࢀࢃࠢ↷").format(bstack11ll_opy_ (u"ࠨ࠮ࠣࠫ↸").join([event[bstack11ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↹")] for event in bstack1ll11l1l_opy_])))
        response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ↺"), cls.request_url(event_url), bstack1ll11l1l_opy_, config)
        bstack1llll1lll111_opy_ = response.json()
    @classmethod
    def bstack1ll1lll1_opy_(cls, bstack1ll11l1l_opy_, event_url=bstack11ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ↻")):
        logger.debug(bstack11ll_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡤࡨࡩࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ↼").format(bstack1ll11l1l_opy_[bstack11ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↽")]))
        if not bstack1111l1l11l_opy_.bstack1llll1l111ll_opy_(bstack1ll11l1l_opy_[bstack11ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↾")]):
            logger.debug(bstack11ll_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡔ࡯ࡵࠢࡤࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ↿").format(bstack1ll11l1l_opy_[bstack11ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇀")]))
            return
        bstack11lll1l1ll_opy_ = bstack1111l1l11l_opy_.bstack1llll11lllll_opy_(bstack1ll11l1l_opy_[bstack11ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇁")], bstack1ll11l1l_opy_.get(bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⇂")))
        if bstack11lll1l1ll_opy_ != None:
            if bstack1ll11l1l_opy_.get(bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ⇃")) != None:
                bstack1ll11l1l_opy_[bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ⇄")][bstack11ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ⇅")] = bstack11lll1l1ll_opy_
            else:
                bstack1ll11l1l_opy_[bstack11ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭⇆")] = bstack11lll1l1ll_opy_
        if event_url == bstack11ll_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ⇇"):
            cls.bstack1llll11l111l_opy_()
            logger.debug(bstack11ll_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ⇈").format(bstack1ll11l1l_opy_[bstack11ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇉")]))
            cls.bstack11l11l11l11_opy_.add(bstack1ll11l1l_opy_)
        elif event_url == bstack11ll_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇊"):
            cls.post_data([bstack1ll11l1l_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l11l1ll_opy_(cls, logs):
        for log in logs:
            bstack1llll11ll1l1_opy_ = {
                bstack11ll_opy_ (u"࠭࡫ࡪࡰࡧࠫ⇋"): bstack11ll_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩ⇌"),
                bstack11ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ⇍"): log[bstack11ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⇎")],
                bstack11ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⇏"): log[bstack11ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇐")],
                bstack11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬ⇑"): {},
                bstack11ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇒"): log[bstack11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇓")],
            }
            if bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇔") in log:
                bstack1llll11ll1l1_opy_[bstack11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇕")] = log[bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇖")]
            elif bstack11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇗") in log:
                bstack1llll11ll1l1_opy_[bstack11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇘")] = log[bstack11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇙")]
            cls.bstack1ll1lll1_opy_({
                bstack11ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇚"): bstack11ll_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⇛"),
                bstack11ll_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ⇜"): [bstack1llll11ll1l1_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l11l11_opy_(cls, steps):
        bstack1llll11l1ll1_opy_ = []
        for step in steps:
            bstack1llll11lll11_opy_ = {
                bstack11ll_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ⇝"): bstack11ll_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧ⇞"),
                bstack11ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⇟"): step[bstack11ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇠")],
                bstack11ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇡"): step[bstack11ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇢")],
                bstack11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇣"): step[bstack11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⇤")],
                bstack11ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⇥"): step[bstack11ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⇦")]
            }
            if bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇧") in step:
                bstack1llll11lll11_opy_[bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇨")] = step[bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇩")]
            elif bstack11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇪") in step:
                bstack1llll11lll11_opy_[bstack11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇫")] = step[bstack11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇬")]
            bstack1llll11l1ll1_opy_.append(bstack1llll11lll11_opy_)
        cls.bstack1ll1lll1_opy_({
            bstack11ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇭"): bstack11ll_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ⇮"),
            bstack11ll_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ⇯"): bstack1llll11l1ll1_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack111111ll1l_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1l1l11lll_opy_(cls, screenshot):
        cls.bstack1ll1lll1_opy_({
            bstack11ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇰"): bstack11ll_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⇱"),
            bstack11ll_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⇲"): [{
                bstack11ll_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⇳"): bstack11ll_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧ⇴"),
                bstack11ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇵"): datetime.datetime.utcnow().isoformat() + bstack11ll_opy_ (u"࡛ࠧࠩ⇶"),
                bstack11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇷"): screenshot[bstack11ll_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ⇸")],
                bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇹"): screenshot[bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇺")]
            }]
        }, event_url=bstack11ll_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇻"))
    @classmethod
    @error_handler(class_method=True)
    def bstack11ll1l11l1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1ll1lll1_opy_({
            bstack11ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇼"): bstack11ll_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ⇽"),
            bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ⇾"): {
                bstack11ll_opy_ (u"ࠤࡸࡹ࡮ࡪࠢ⇿"): cls.current_test_uuid(),
                bstack11ll_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤ∀"): cls.bstack1l1lll1l_opy_(driver)
            }
        })
    @classmethod
    def bstack1lll1l11_opy_(cls, event: str, bstack1ll11l1l_opy_: bstack1llll11l_opy_):
        bstack1l11l111_opy_ = {
            bstack11ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ∁"): event,
            bstack1ll11l1l_opy_.event_key(): bstack1ll11l1l_opy_.bstack1ll11lll_opy_(event)
        }
        cls.bstack1ll1lll1_opy_(bstack1l11l111_opy_)
        result = getattr(bstack1ll11l1l_opy_, bstack11ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ∂"), None)
        if event == bstack11ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ∃"):
            threading.current_thread().bstackTestMeta = {bstack11ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ∄"): bstack11ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ∅")}
        elif event == bstack11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ∆"):
            threading.current_thread().bstackTestMeta = {bstack11ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ∇"): getattr(result, bstack11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ∈"), bstack11ll_opy_ (u"ࠬ࠭∉"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ∊"), None) is None or os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ∋")] == bstack11ll_opy_ (u"ࠣࡰࡸࡰࡱࠨ∌")) and (os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ∍"), None) is None or os.environ[bstack11ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ∎")] == bstack11ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ∏")):
            return False
        return True
    @staticmethod
    def bstack1llll11l11ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l111l1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ∐"): bstack11ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ∑"),
            bstack11ll_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪ−"): bstack11ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭∓")
        }
        if os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭∔"), None):
            headers[bstack11ll_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ∕")] = bstack11ll_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧ∖").format(os.environ[bstack11ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤ∗")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11ll_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ∘").format(bstack1llll11ll11l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ∙"), None)
    @staticmethod
    def bstack1l1lll1l_opy_(driver):
        return {
            bstack1111lll11l1_opy_(): bstack1111l1lll11_opy_(driver)
        }
    @staticmethod
    def bstack1llll111llll_opy_(exception_info, report):
        return [{bstack11ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ√"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1111111ll1_opy_(typename):
        if bstack11ll_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ∛") in typename:
            return bstack11ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ∜")
        return bstack11ll_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ∝")