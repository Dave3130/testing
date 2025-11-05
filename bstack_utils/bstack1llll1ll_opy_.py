# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l11l1l11_opy_, bstack111l111lll1_opy_, bstack11ll11ll1l_opy_, error_handler, bstack1111lll1l1l_opy_, bstack1111l1ll1l1_opy_, bstack111l11ll1l1_opy_, bstack1ll111ll_opy_, bstack1l1l1ll1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l111l1l1l_opy_ import bstack111l1ll11ll_opy_
import bstack_utils.bstack111111ll1l_opy_ as bstack1111llll11_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1l11l1l1_opy_
import bstack_utils.accessibility as bstack1lll11l11_opy_
from bstack_utils.bstack11lll1l1l_opy_ import bstack11lll1l1l_opy_
from bstack_utils.bstack1lll1l11_opy_ import bstack1ll11l1l_opy_
from bstack_utils.constants import bstack11ll1l1l1_opy_
bstack1llll111ll11_opy_ = bstack11ll1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡨࡵ࡬࡭ࡧࡦࡸࡴࡸ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ⅑")
logger = logging.getLogger(__name__)
class bstack1ll1l111_opy_:
    bstack11l111l1l1l_opy_ = None
    bs_config = None
    bstack111l11l11l_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11ll11l1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def launch(cls, bs_config, bstack111l11l11l_opy_):
        cls.bs_config = bs_config
        cls.bstack111l11l11l_opy_ = bstack111l11l11l_opy_
        try:
            cls.bstack1llll11l1ll1_opy_()
            bstack1llll1l11lll_opy_ = bstack111l11l1l11_opy_(bs_config)
            bstack1llll1l1l11l_opy_ = bstack111l111lll1_opy_(bs_config)
            data = bstack1111llll11_opy_.bstack1llll11l11l1_opy_(bs_config, bstack111l11l11l_opy_)
            config = {
                bstack11ll1ll_opy_ (u"ࠫࡦࡻࡴࡩࠩ⅒"): (bstack1llll1l11lll_opy_, bstack1llll1l1l11l_opy_),
                bstack11ll1ll_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭⅓"): cls.default_headers()
            }
            response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"࠭ࡐࡐࡕࡗࠫ⅔"), cls.request_url(bstack11ll1ll_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠸࠯ࡣࡷ࡬ࡰࡩࡹࠧ⅕")), data, config)
            if response.status_code != 200:
                bstack1111l11111_opy_ = response.json()
                if bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ⅖")] == False:
                    cls.bstack1llll11l11ll_opy_(bstack1111l11111_opy_)
                    return
                cls.bstack1llll111l1l1_opy_(bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")])
                cls.bstack1llll11l1l11_opy_(bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⅘")])
                return None
            bstack1llll11l1l1l_opy_ = cls.bstack1llll111l1ll_opy_(response)
            return bstack1llll11l1l1l_opy_, response.json()
        except Exception as error:
            logger.error(bstack11ll1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡧࡱࡵࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࡻࡾࠤ⅙").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll11l111l_opy_=None):
        if not bstack1l11l1l1_opy_.on() and not bstack1lll11l11_opy_.on():
            return
        if os.environ.get(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⅚")) == bstack11ll1ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ⅛") or os.environ.get(bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⅜")) == bstack11ll1ll_opy_ (u"ࠣࡰࡸࡰࡱࠨ⅝"):
            logger.error(bstack11ll1ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬ⅞"))
            return {
                bstack11ll1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ⅟"): bstack11ll1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪⅠ"),
                bstack11ll1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ⅱ"): bstack11ll1ll_opy_ (u"࠭ࡔࡰ࡭ࡨࡲ࠴ࡨࡵࡪ࡮ࡧࡍࡉࠦࡩࡴࠢࡸࡲࡩ࡫ࡦࡪࡰࡨࡨ࠱ࠦࡢࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠ࡮࡫ࡪ࡬ࡹࠦࡨࡢࡸࡨࠤ࡫ࡧࡩ࡭ࡧࡧࠫⅢ")
            }
        try:
            cls.bstack11l111l1l1l_opy_.shutdown()
            data = {
                bstack11ll1ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬⅣ"): bstack1ll111ll_opy_()
            }
            if not bstack1llll11l111l_opy_ is None:
                data[bstack11ll1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡱࡪࡺࡡࡥࡣࡷࡥࠬⅤ")] = [{
                    bstack11ll1ll_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩⅥ"): bstack11ll1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡠ࡭࡬ࡰࡱ࡫ࡤࠨⅦ"),
                    bstack11ll1ll_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࠫⅧ"): bstack1llll11l111l_opy_
                }]
            config = {
                bstack11ll1ll_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭Ⅸ"): cls.default_headers()
            }
            bstack11ll11111ll_opy_ = bstack11ll1ll_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡸࡴࡶࠧⅩ").format(os.environ[bstack11ll1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧⅪ")])
            bstack1llll111l111_opy_ = cls.request_url(bstack11ll11111ll_opy_)
            response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠨࡒࡘࡘࠬⅫ"), bstack1llll111l111_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11ll1ll_opy_ (u"ࠤࡖࡸࡴࡶࠠࡳࡧࡴࡹࡪࡹࡴࠡࡰࡲࡸࠥࡵ࡫ࠣⅬ"))
        except Exception as error:
            logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾࠿ࠦࠢⅭ") + str(error))
            return {
                bstack11ll1ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫⅮ"): bstack11ll1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫⅯ"),
                bstack11ll1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧⅰ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll111l1ll_opy_(cls, response):
        bstack1111l11111_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11l1l1l_opy_ = {}
        if bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠧ࡫ࡹࡷࠫⅱ")) is None:
            os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬⅲ")] = bstack11ll1ll_opy_ (u"ࠩࡱࡹࡱࡲࠧⅳ")
        else:
            os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧⅴ")] = bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠫ࡯ࡽࡴࠨⅵ"), bstack11ll1ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪⅶ"))
        os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫⅷ")] = bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅸ"), bstack11ll1ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭ⅹ"))
        logger.info(bstack11ll1ll_opy_ (u"ࠩࡗࡩࡸࡺࡨࡶࡤࠣࡷࡹࡧࡲࡵࡧࡧࠤࡼ࡯ࡴࡩࠢ࡬ࡨ࠿ࠦࠧⅺ") + os.getenv(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨⅻ")));
        if bstack1l11l1l1_opy_.bstack11l111ll1l1_opy_(cls.bs_config, cls.bstack111l11l11l_opy_.get(bstack11ll1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬⅼ"), bstack11ll1ll_opy_ (u"ࠬ࠭ⅽ"))) is True:
            bstack11ll111l1ll_opy_, build_hashed_id, bstack1llll11ll1ll_opy_ = cls.bstack1llll11lll1l_opy_(bstack1111l11111_opy_)
            if bstack11ll111l1ll_opy_ != None and build_hashed_id != None:
                bstack1llll11l1l1l_opy_[bstack11ll1ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ⅾ")] = {
                    bstack11ll1ll_opy_ (u"ࠧ࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠪⅿ"): bstack11ll111l1ll_opy_,
                    bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪↀ"): build_hashed_id,
                    bstack11ll1ll_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ↁ"): bstack1llll11ll1ll_opy_
                }
            else:
                bstack1llll11l1l1l_opy_[bstack11ll1ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪↂ")] = {}
        else:
            bstack1llll11l1l1l_opy_[bstack11ll1ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫↃ")] = {}
        bstack1llll11ll11l_opy_, build_hashed_id = cls.bstack1llll111llll_opy_(bstack1111l11111_opy_)
        if bstack1llll11ll11l_opy_ != None and build_hashed_id != None:
            bstack1llll11l1l1l_opy_[bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬↄ")] = {
                bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶ࡫ࡣࡹࡵ࡫ࡦࡰࠪↅ"): bstack1llll11ll11l_opy_,
                bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩↆ"): build_hashed_id,
            }
        else:
            bstack1llll11l1l1l_opy_[bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨↇ")] = {}
        if bstack1llll11l1l1l_opy_[bstack11ll1ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩↈ")].get(bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ↉")) != None or bstack1llll11l1l1l_opy_[bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ↊")].get(bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ↋")) != None:
            cls.bstack1llll1111lll_opy_(bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡪࡸࡶࠪ↌")), bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ↍")))
        return bstack1llll11l1l1l_opy_
    @classmethod
    def bstack1llll11lll1l_opy_(cls, bstack1111l11111_opy_):
        if bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ↎")) == None:
            cls.bstack1llll111l1l1_opy_()
            return [None, None, None]
        if bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ↏")][bstack11ll1ll_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ←")] != True:
            cls.bstack1llll111l1l1_opy_(bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ↑")])
            return [None, None, None]
        logger.debug(bstack11ll1ll_opy_ (u"ࠬࢁࡽࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧ→").format(bstack11ll1l1l1_opy_))
        os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬ↓")] = bstack11ll1ll_opy_ (u"ࠧࡵࡴࡸࡩࠬ↔")
        if bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠨ࡬ࡺࡸࠬ↕")):
            os.environ[bstack11ll1ll_opy_ (u"ࠩࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙࡟ࡇࡑࡕࡣࡈࡘࡁࡔࡊࡢࡖࡊࡖࡏࡓࡖࡌࡒࡌ࠭↖")] = json.dumps({
                bstack11ll1ll_opy_ (u"ࠪࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ↗"): bstack111l11l1l11_opy_(cls.bs_config),
                bstack11ll1ll_opy_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭↘"): bstack111l111lll1_opy_(cls.bs_config)
            })
        if bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ↙")):
            os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬ↚")] = bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ↛")]
        if bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ↜")].get(bstack11ll1ll_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ↝"), {}).get(bstack11ll1ll_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ↞")):
            os.environ[bstack11ll1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ↟")] = str(bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ↠")][bstack11ll1ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ↡")][bstack11ll1ll_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫ↢")])
        else:
            os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩ↣")] = bstack11ll1ll_opy_ (u"ࠤࡱࡹࡱࡲࠢ↤")
        return [bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠪ࡮ࡼࡺࠧ↥")], bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭↦")], os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭↧")]]
    @classmethod
    def bstack1llll111llll_opy_(cls, bstack1111l11111_opy_):
        if bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭↨")) == None:
            cls.bstack1llll11l1l11_opy_()
            return [None, None]
        if bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ↩")][bstack11ll1ll_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ↪")] != True:
            cls.bstack1llll11l1l11_opy_(bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ↫")])
            return [None, None]
        if bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ↬")].get(bstack11ll1ll_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ↭")):
            logger.debug(bstack11ll1ll_opy_ (u"࡚ࠬࡥࡴࡶࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠢࠩ↮"))
            parsed = json.loads(os.getenv(bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ↯"), bstack11ll1ll_opy_ (u"ࠧࡼࡿࠪ↰")))
            capabilities = bstack1111llll11_opy_.bstack1llll111l11l_opy_(bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ↱")][bstack11ll1ll_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ↲")][bstack11ll1ll_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ↳")], bstack11ll1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ↴"), bstack11ll1ll_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫ↵"))
            bstack1llll11ll11l_opy_ = capabilities[bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫ↶")]
            os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ↷")] = bstack1llll11ll11l_opy_
            if bstack11ll1ll_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ↸") in bstack1111l11111_opy_ and bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠤࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠣ↹")) is None:
                parsed[bstack11ll1ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ↺")] = capabilities[bstack11ll1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ↻")]
            os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭↼")] = json.dumps(parsed)
            scripts = bstack1111llll11_opy_.bstack1llll111l11l_opy_(bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭↽")][bstack11ll1ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ↾")][bstack11ll1ll_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ↿")], bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ⇀"), bstack11ll1ll_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࠫ⇁"))
            bstack11lll1l1l_opy_.bstack1ll11lllll_opy_(scripts)
            commands = bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⇂")][bstack11ll1ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭⇃")][bstack11ll1ll_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࡕࡱ࡚ࡶࡦࡶࠧ⇄")].get(bstack11ll1ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ⇅"))
            bstack11lll1l1l_opy_.bstack1lllll1111ll_opy_(commands)
            bstack1llll1llll11_opy_ = capabilities.get(bstack11ll1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⇆"))
            bstack11lll1l1l_opy_.bstack1llll1llllll_opy_(bstack1llll1llll11_opy_)
            bstack11lll1l1l_opy_.store()
        return [bstack1llll11ll11l_opy_, bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⇇")]]
    @classmethod
    def bstack1llll111l1l1_opy_(cls, response=None):
        os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ⇈")] = bstack11ll1ll_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ⇉")
        os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⇊")] = bstack11ll1ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ⇋")
        os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭⇌")] = bstack11ll1ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ⇍")
        os.environ[bstack11ll1ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨ⇎")] = bstack11ll1ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ⇏")
        os.environ[bstack11ll1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ⇐")] = bstack11ll1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ⇑")
        cls.bstack1llll11l11ll_opy_(response, bstack11ll1ll_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨ⇒"))
        return [None, None, None]
    @classmethod
    def bstack1llll11l1l11_opy_(cls, response=None):
        os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⇓")] = bstack11ll1ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭⇔")
        os.environ[bstack11ll1ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ⇕")] = bstack11ll1ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ⇖")
        os.environ[bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⇗")] = bstack11ll1ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ⇘")
        cls.bstack1llll11l11ll_opy_(response, bstack11ll1ll_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠨ⇙"))
        return [None, None, None]
    @classmethod
    def bstack1llll1111lll_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⇚")] = jwt
        os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭⇛")] = build_hashed_id
    @classmethod
    def bstack1llll11l11ll_opy_(cls, response=None, product=bstack11ll1ll_opy_ (u"ࠤࠥ⇜")):
        if response == None or response.get(bstack11ll1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪ⇝")) == None:
            logger.error(product + bstack11ll1ll_opy_ (u"ࠦࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠨ⇞"))
            return
        for error in response[bstack11ll1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ⇟")]:
            bstack1111l11l1l1_opy_ = error[bstack11ll1ll_opy_ (u"࠭࡫ࡦࡻࠪ⇠")]
            error_message = error[bstack11ll1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇡")]
            if error_message:
                if bstack1111l11l1l1_opy_ == bstack11ll1ll_opy_ (u"ࠣࡇࡕࡖࡔࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡅࡇࡑࡍࡊࡊࠢ⇢"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11ll1ll_opy_ (u"ࠤࡇࡥࡹࡧࠠࡶࡲ࡯ࡳࡦࡪࠠࡵࡱࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࠥ⇣") + product + bstack11ll1ll_opy_ (u"ࠥࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣ⇤"))
    @classmethod
    def bstack1llll11l1ll1_opy_(cls):
        if cls.bstack11l111l1l1l_opy_ is not None:
            return
        cls.bstack11l111l1l1l_opy_ = bstack111l1ll11ll_opy_(cls.post_data)
        cls.bstack11l111l1l1l_opy_.start()
    @classmethod
    def bstack1llll11l_opy_(cls):
        if cls.bstack11l111l1l1l_opy_ is None:
            return
        cls.bstack11l111l1l1l_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l11l1ll_opy_, event_url=bstack11ll1ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ⇥")):
        config = {
            bstack11ll1ll_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭⇦"): cls.default_headers()
        }
        logger.debug(bstack11ll1ll_opy_ (u"ࠨࡰࡰࡵࡷࡣࡩࡧࡴࡢ࠼ࠣࡗࡪࡴࡤࡪࡰࡪࠤࡩࡧࡴࡢࠢࡷࡳࠥࡺࡥࡴࡶ࡫ࡹࡧࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࡵࠣࡿࢂࠨ⇧").format(bstack11ll1ll_opy_ (u"ࠧ࠭ࠢࠪ⇨").join([event[bstack11ll1ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇩")] for event in bstack1l11l1ll_opy_])))
        response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ⇪"), cls.request_url(event_url), bstack1l11l1ll_opy_, config)
        bstack1llll1l11111_opy_ = response.json()
    @classmethod
    def bstack11llll1l_opy_(cls, bstack1l11l1ll_opy_, event_url=bstack11ll1ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ⇫")):
        logger.debug(bstack11ll1ll_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡣࡧࡨࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ⇬").format(bstack1l11l1ll_opy_[bstack11ll1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇭")]))
        if not bstack1111llll11_opy_.bstack1llll11l1111_opy_(bstack1l11l1ll_opy_[bstack11ll1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇮")]):
            logger.debug(bstack11ll1ll_opy_ (u"ࠢࡴࡧࡱࡨࡤࡪࡡࡵࡣ࠽ࠤࡓࡵࡴࠡࡣࡧࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ⇯").format(bstack1l11l1ll_opy_[bstack11ll1ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇰")]))
            return
        bstack1ll11ll1l1_opy_ = bstack1111llll11_opy_.bstack1llll11llll1_opy_(bstack1l11l1ll_opy_[bstack11ll1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇱")], bstack1l11l1ll_opy_.get(bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ⇲")))
        if bstack1ll11ll1l1_opy_ != None:
            if bstack1l11l1ll_opy_.get(bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⇳")) != None:
                bstack1l11l1ll_opy_[bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ⇴")][bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ⇵")] = bstack1ll11ll1l1_opy_
            else:
                bstack1l11l1ll_opy_[bstack11ll1ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ⇶")] = bstack1ll11ll1l1_opy_
        if event_url == bstack11ll1ll_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ⇷"):
            cls.bstack1llll11l1ll1_opy_()
            logger.debug(bstack11ll1ll_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡁࡥࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ⇸").format(bstack1l11l1ll_opy_[bstack11ll1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇹")]))
            cls.bstack11l111l1l1l_opy_.add(bstack1l11l1ll_opy_)
        elif event_url == bstack11ll1ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ⇺"):
            cls.post_data([bstack1l11l1ll_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l1111ll_opy_(cls, logs):
        for log in logs:
            bstack1llll11l1lll_opy_ = {
                bstack11ll1ll_opy_ (u"ࠬࡱࡩ࡯ࡦࠪ⇻"): bstack11ll1ll_opy_ (u"࠭ࡔࡆࡕࡗࡣࡑࡕࡇࠨ⇼"),
                bstack11ll1ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⇽"): log[bstack11ll1ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ⇾")],
                bstack11ll1ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⇿"): log[bstack11ll1ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭∀")],
                bstack11ll1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡡࡵࡩࡸࡶ࡯࡯ࡵࡨࠫ∁"): {},
                bstack11ll1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭∂"): log[bstack11ll1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ∃")],
            }
            if bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ∄") in log:
                bstack1llll11l1lll_opy_[bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ∅")] = log[bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∆")]
            elif bstack11ll1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ∇") in log:
                bstack1llll11l1lll_opy_[bstack11ll1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ∈")] = log[bstack11ll1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ∉")]
            cls.bstack11llll1l_opy_({
                bstack11ll1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ∊"): bstack11ll1ll_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ∋"),
                bstack11ll1ll_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭∌"): [bstack1llll11l1lll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11ll111_opy_(cls, steps):
        bstack1llll11ll1l1_opy_ = []
        for step in steps:
            bstack1llll111lll1_opy_ = {
                bstack11ll1ll_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ∍"): bstack11ll1ll_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡗࡉࡕ࠭∎"),
                bstack11ll1ll_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ∏"): step[bstack11ll1ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ∐")],
                bstack11ll1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ∑"): step[bstack11ll1ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ−")],
                bstack11ll1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ∓"): step[bstack11ll1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ∔")],
                bstack11ll1ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ∕"): step[bstack11ll1ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭∖")]
            }
            if bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ∗") in step:
                bstack1llll111lll1_opy_[bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭∘")] = step[bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ∙")]
            elif bstack11ll1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ√") in step:
                bstack1llll111lll1_opy_[bstack11ll1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∛")] = step[bstack11ll1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ∜")]
            bstack1llll11ll1l1_opy_.append(bstack1llll111lll1_opy_)
        cls.bstack11llll1l_opy_({
            bstack11ll1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ∝"): bstack11ll1ll_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ∞"),
            bstack11ll1ll_opy_ (u"࠭࡬ࡰࡩࡶࠫ∟"): bstack1llll11ll1l1_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11l1lll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1ll11ll1ll_opy_(cls, screenshot):
        cls.bstack11llll1l_opy_({
            bstack11ll1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ∠"): bstack11ll1ll_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ∡"),
            bstack11ll1ll_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ∢"): [{
                bstack11ll1ll_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ∣"): bstack11ll1ll_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࠭∤"),
                bstack11ll1ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ∥"): datetime.datetime.utcnow().isoformat() + bstack11ll1ll_opy_ (u"࡚࠭ࠨ∦"),
                bstack11ll1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ∧"): screenshot[bstack11ll1ll_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ∨")],
                bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∩"): screenshot[bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ∪")]
            }]
        }, event_url=bstack11ll1ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ∫"))
    @classmethod
    @error_handler(class_method=True)
    def bstack11l1lllll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11llll1l_opy_({
            bstack11ll1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ∬"): bstack11ll1ll_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ∭"),
            bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ∮"): {
                bstack11ll1ll_opy_ (u"ࠣࡷࡸ࡭ࡩࠨ∯"): cls.current_test_uuid(),
                bstack11ll1ll_opy_ (u"ࠤ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠣ∰"): cls.bstack1ll1ll1l_opy_(driver)
            }
        })
    @classmethod
    def bstack1l1lll1l_opy_(cls, event: str, bstack1l11l1ll_opy_: bstack1ll11l1l_opy_):
        bstack11llll11_opy_ = {
            bstack11ll1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ∱"): event,
            bstack1l11l1ll_opy_.event_key(): bstack1l11l1ll_opy_.bstack1ll1lll1_opy_(event)
        }
        cls.bstack11llll1l_opy_(bstack11llll11_opy_)
        result = getattr(bstack1l11l1ll_opy_, bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ∲"), None)
        if event == bstack11ll1ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭∳"):
            threading.current_thread().bstackTestMeta = {bstack11ll1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭∴"): bstack11ll1ll_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ∵")}
        elif event == bstack11ll1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ∶"):
            threading.current_thread().bstackTestMeta = {bstack11ll1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ∷"): getattr(result, bstack11ll1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ∸"), bstack11ll1ll_opy_ (u"ࠫࠬ∹"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ∺"), None) is None or os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ∻")] == bstack11ll1ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ∼")) and (os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭∽"), None) is None or os.environ[bstack11ll1ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ∾")] == bstack11ll1ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ∿")):
            return False
        return True
    @staticmethod
    def bstack1llll111ll1l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1l111_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11ll1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ≀"): bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ≁"),
            bstack11ll1ll_opy_ (u"࠭ࡘ࠮ࡄࡖࡘࡆࡉࡋ࠮ࡖࡈࡗ࡙ࡕࡐࡔࠩ≂"): bstack11ll1ll_opy_ (u"ࠧࡵࡴࡸࡩࠬ≃")
        }
        if os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ≄"), None):
            headers[bstack11ll1ll_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ≅")] = bstack11ll1ll_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭≆").format(os.environ[bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠣ≇")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11ll1ll_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫ≈").format(bstack1llll111ll11_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ≉"), None)
    @staticmethod
    def bstack1ll1ll1l_opy_(driver):
        return {
            bstack1111lll1l1l_opy_(): bstack1111l1ll1l1_opy_(driver)
        }
    @staticmethod
    def bstack1llll11lll11_opy_(exception_info, report):
        return [{bstack11ll1ll_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪ≊"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1111111l11_opy_(typename):
        if bstack11ll1ll_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦ≋") in typename:
            return bstack11ll1ll_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥ≌")
        return bstack11ll1ll_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦ≍")