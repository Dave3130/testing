# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1l1111l_opy_, bstack1111ll1l11l_opy_, bstack111ll1l111_opy_, error_handler, bstack111l11l11ll_opy_, bstack1111l111ll1_opy_, bstack1111ll1111l_opy_, bstack1ll11lll_opy_, bstack1llll11l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l111ll111_opy_ import bstack111l1ll11l1_opy_
import bstack_utils.bstack111ll1111_opy_ as bstack11l1lll11l_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack11llll1l_opy_
import bstack_utils.accessibility as bstack1111111l_opy_
from bstack_utils.bstack1l1ll1lll1_opy_ import bstack1l1ll1lll1_opy_
from bstack_utils.bstack1llll1ll_opy_ import bstack1l1ll11l_opy_
from bstack_utils.constants import bstack1l111l11l_opy_
bstack1llll111lll1_opy_ = bstack11l1111_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡦࡳࡱࡲࡥࡤࡶࡲࡶ࠲ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ⅏")
logger = logging.getLogger(__name__)
class bstack1l11l1l1_opy_:
    bstack11l111ll111_opy_ = None
    bs_config = None
    bstack111l1llll1_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l111l1l_opy_, stage=STAGE.bstack1111ll111_opy_)
    def launch(cls, bs_config, bstack111l1llll1_opy_):
        cls.bs_config = bs_config
        cls.bstack111l1llll1_opy_ = bstack111l1llll1_opy_
        try:
            cls.bstack1llll111ll11_opy_()
            bstack1llll1lll1l1_opy_ = bstack111l1l1111l_opy_(bs_config)
            bstack1llll1l11lll_opy_ = bstack1111ll1l11l_opy_(bs_config)
            data = bstack11l1lll11l_opy_.bstack1llll11lll1l_opy_(bs_config, bstack111l1llll1_opy_)
            config = {
                bstack11l1111_opy_ (u"ࠩࡤࡹࡹ࡮ࠧ⅐"): (bstack1llll1lll1l1_opy_, bstack1llll1l11lll_opy_),
                bstack11l1111_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫ⅑"): cls.default_headers()
            }
            response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"ࠫࡕࡕࡓࡕࠩ⅒"), cls.request_url(bstack11l1111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠶࠴ࡨࡵࡪ࡮ࡧࡷࠬ⅓")), data, config)
            if response.status_code != 200:
                bstack1111llll1_opy_ = response.json()
                if bstack1111llll1_opy_[bstack11l1111_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ⅔")] == False:
                    cls.bstack1llll11l11ll_opy_(bstack1111llll1_opy_)
                    return
                cls.bstack1llll11ll11l_opy_(bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ⅕")])
                cls.bstack1llll11lll11_opy_(bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⅖")])
                return None
            bstack1llll11ll1l1_opy_ = cls.bstack1llll11l11l1_opy_(response)
            return bstack1llll11ll1l1_opy_, response.json()
        except Exception as error:
            logger.error(bstack11l1111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࢀࢃࠢ⅗").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll11l1lll_opy_=None):
        if not bstack11llll1l_opy_.on() and not bstack1111111l_opy_.on():
            return
        if os.environ.get(bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⅘")) == bstack11l1111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⅙") or os.environ.get(bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ⅚")) == bstack11l1111_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ⅛"):
            logger.error(bstack11l1111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡳࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࡐ࡭ࡸࡹࡩ࡯ࡩࠣࡥࡺࡺࡨࡦࡰࡷ࡭ࡨࡧࡴࡪࡱࡱࠤࡹࡵ࡫ࡦࡰࠪ⅜"))
            return {
                bstack11l1111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⅝"): bstack11l1111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ⅞"),
                bstack11l1111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⅟"): bstack11l1111_opy_ (u"࡙ࠫࡵ࡫ࡦࡰ࠲ࡦࡺ࡯࡬ࡥࡋࡇࠤ࡮ࡹࠠࡶࡰࡧࡩ࡫࡯࡮ࡦࡦ࠯ࠤࡧࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥࡳࡩࡨࡪࡷࠤ࡭ࡧࡶࡦࠢࡩࡥ࡮ࡲࡥࡥࠩⅠ")
            }
        try:
            cls.bstack11l111ll111_opy_.shutdown()
            data = {
                bstack11l1111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪⅡ"): bstack1ll11lll_opy_()
            }
            if not bstack1llll11l1lll_opy_ is None:
                data[bstack11l1111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠ࡯ࡨࡸࡦࡪࡡࡵࡣࠪⅢ")] = [{
                    bstack11l1111_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧⅣ"): bstack11l1111_opy_ (u"ࠨࡷࡶࡩࡷࡥ࡫ࡪ࡮࡯ࡩࡩ࠭Ⅴ"),
                    bstack11l1111_opy_ (u"ࠩࡶ࡭࡬ࡴࡡ࡭ࠩⅥ"): bstack1llll11l1lll_opy_
                }]
            config = {
                bstack11l1111_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫⅦ"): cls.default_headers()
            }
            bstack11ll111l111_opy_ = bstack11l1111_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡴࡶࡲࡴࠬⅧ").format(os.environ[bstack11l1111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥⅨ")])
            bstack1llll11l1l1l_opy_ = cls.request_url(bstack11ll111l111_opy_)
            response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"࠭ࡐࡖࡖࠪⅩ"), bstack1llll11l1l1l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11l1111_opy_ (u"ࠢࡔࡶࡲࡴࠥࡸࡥࡲࡷࡨࡷࡹࠦ࡮ࡰࡶࠣࡳࡰࠨⅪ"))
        except Exception as error:
            logger.error(bstack11l1111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡴࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡖࡨࡷࡹࡎࡵࡣ࠼࠽ࠤࠧⅫ") + str(error))
            return {
                bstack11l1111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩⅬ"): bstack11l1111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩⅭ"),
                bstack11l1111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬⅮ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l11l1_opy_(cls, response):
        bstack1111llll1_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11ll1l1_opy_ = {}
        if bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠬࡰࡷࡵࠩⅯ")) is None:
            os.environ[bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪⅰ")] = bstack11l1111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅱ")
        else:
            os.environ[bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬⅲ")] = bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠩ࡭ࡻࡹ࠭ⅳ"), bstack11l1111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨⅴ"))
        os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩⅵ")] = bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧⅶ"), bstack11l1111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫⅷ"))
        logger.info(bstack11l1111_opy_ (u"ࠧࡕࡧࡶࡸ࡭ࡻࡢࠡࡵࡷࡥࡷࡺࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡪࡦ࠽ࠤࠬⅸ") + os.getenv(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ⅹ")));
        if bstack11llll1l_opy_.bstack11l111l1ll1_opy_(cls.bs_config, cls.bstack111l1llll1_opy_.get(bstack11l1111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪⅺ"), bstack11l1111_opy_ (u"ࠪࠫⅻ"))) is True:
            bstack11ll1111l1l_opy_, build_hashed_id, bstack1llll11l111l_opy_ = cls.bstack1llll111ll1l_opy_(bstack1111llll1_opy_)
            if bstack11ll1111l1l_opy_ != None and build_hashed_id != None:
                bstack1llll11ll1l1_opy_[bstack11l1111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫⅼ")] = {
                    bstack11l1111_opy_ (u"ࠬࡰࡷࡵࡡࡷࡳࡰ࡫࡮ࠨⅽ"): bstack11ll1111l1l_opy_,
                    bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅾ"): build_hashed_id,
                    bstack11l1111_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫⅿ"): bstack1llll11l111l_opy_
                }
            else:
                bstack1llll11ll1l1_opy_[bstack11l1111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨↀ")] = {}
        else:
            bstack1llll11ll1l1_opy_[bstack11l1111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩↁ")] = {}
        bstack1llll111l11l_opy_, build_hashed_id = cls.bstack1llll111llll_opy_(bstack1111llll1_opy_)
        if bstack1llll111l11l_opy_ != None and build_hashed_id != None:
            bstack1llll11ll1l1_opy_[bstack11l1111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪↂ")] = {
                bstack11l1111_opy_ (u"ࠫࡦࡻࡴࡩࡡࡷࡳࡰ࡫࡮ࠨↃ"): bstack1llll111l11l_opy_,
                bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧↄ"): build_hashed_id,
            }
        else:
            bstack1llll11ll1l1_opy_[bstack11l1111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ↅ")] = {}
        if bstack1llll11ll1l1_opy_[bstack11l1111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧↆ")].get(bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪↇ")) != None or bstack1llll11ll1l1_opy_[bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩↈ")].get(bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ↉")) != None:
            cls.bstack1llll11ll111_opy_(bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠫ࡯ࡽࡴࠨ↊")), bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ↋")))
        return bstack1llll11ll1l1_opy_
    @classmethod
    def bstack1llll111ll1l_opy_(cls, bstack1111llll1_opy_):
        if bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭↌")) == None:
            cls.bstack1llll11ll11l_opy_()
            return [None, None, None]
        if bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ↍")][bstack11l1111_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ↎")] != True:
            cls.bstack1llll11ll11l_opy_(bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ↏")])
            return [None, None, None]
        logger.debug(bstack11l1111_opy_ (u"ࠪࡿࢂࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠥࠬ←").format(bstack1l111l11l_opy_))
        os.environ[bstack11l1111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪ↑")] = bstack11l1111_opy_ (u"ࠬࡺࡲࡶࡧࠪ→")
        if bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"࠭ࡪࡸࡶࠪ↓")):
            os.environ[bstack11l1111_opy_ (u"ࠧࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࡤࡌࡏࡓࡡࡆࡖࡆ࡙ࡈࡠࡔࡈࡔࡔࡘࡔࡊࡐࡊࠫ↔")] = json.dumps({
                bstack11l1111_opy_ (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࠪ↕"): bstack111l1l1111l_opy_(cls.bs_config),
                bstack11l1111_opy_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫ↖"): bstack1111ll1l11l_opy_(cls.bs_config)
            })
        if bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ↗")):
            os.environ[bstack11l1111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪ↘")] = bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ↙")]
        if bstack1111llll1_opy_[bstack11l1111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭↚")].get(bstack11l1111_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ↛"), {}).get(bstack11l1111_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬ↜")):
            os.environ[bstack11l1111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪ↝")] = str(bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ↞")][bstack11l1111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ↟")][bstack11l1111_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ↠")])
        else:
            os.environ[bstack11l1111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧ↡")] = bstack11l1111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ↢")
        return [bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠨ࡬ࡺࡸࠬ↣")], bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ↤")], os.environ[bstack11l1111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ↥")]]
    @classmethod
    def bstack1llll111llll_opy_(cls, bstack1111llll1_opy_):
        if bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ↦")) == None:
            cls.bstack1llll11lll11_opy_()
            return [None, None]
        if bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ↧")][bstack11l1111_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ↨")] != True:
            cls.bstack1llll11lll11_opy_(bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ↩")])
            return [None, None]
        if bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ↪")].get(bstack11l1111_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ↫")):
            logger.debug(bstack11l1111_opy_ (u"ࠪࡘࡪࡹࡴࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧ↬"))
            parsed = json.loads(os.getenv(bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ↭"), bstack11l1111_opy_ (u"ࠬࢁࡽࠨ↮")))
            capabilities = bstack11l1lll11l_opy_.bstack1llll111l111_opy_(bstack1111llll1_opy_[bstack11l1111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭↯")][bstack11l1111_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ↰")][bstack11l1111_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ↱")], bstack11l1111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ↲"), bstack11l1111_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ↳"))
            bstack1llll111l11l_opy_ = capabilities[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠩ↴")]
            os.environ[bstack11l1111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ↵")] = bstack1llll111l11l_opy_
            if bstack11l1111_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣ↶") in bstack1111llll1_opy_ and bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠢࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ↷")) is None:
                parsed[bstack11l1111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ↸")] = capabilities[bstack11l1111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ↹")]
            os.environ[bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ↺")] = json.dumps(parsed)
            scripts = bstack11l1lll11l_opy_.bstack1llll111l111_opy_(bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ↻")][bstack11l1111_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭↼")][bstack11l1111_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ↽")], bstack11l1111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ↾"), bstack11l1111_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࠩ↿"))
            bstack1l1ll1lll1_opy_.bstack1l11lll1l_opy_(scripts)
            commands = bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⇀")][bstack11l1111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⇁")][bstack11l1111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࡚࡯ࡘࡴࡤࡴࠬ⇂")].get(bstack11l1111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ⇃"))
            bstack1l1ll1lll1_opy_.bstack1llll1llllll_opy_(commands)
            bstack1lllll11111l_opy_ = capabilities.get(bstack11l1111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⇄"))
            bstack1l1ll1lll1_opy_.bstack1lllll1111l1_opy_(bstack1lllll11111l_opy_)
            bstack1l1ll1lll1_opy_.store()
        return [bstack1llll111l11l_opy_, bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ⇅")]]
    @classmethod
    def bstack1llll11ll11l_opy_(cls, response=None):
        os.environ[bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭⇆")] = bstack11l1111_opy_ (u"ࠩࡱࡹࡱࡲࠧ⇇")
        os.environ[bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⇈")] = bstack11l1111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ⇉")
        os.environ[bstack11l1111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫ⇊")] = bstack11l1111_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ⇋")
        os.environ[bstack11l1111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭⇌")] = bstack11l1111_opy_ (u"ࠣࡰࡸࡰࡱࠨ⇍")
        os.environ[bstack11l1111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪ⇎")] = bstack11l1111_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ⇏")
        cls.bstack1llll11l11ll_opy_(response, bstack11l1111_opy_ (u"ࠦࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠦ⇐"))
        return [None, None, None]
    @classmethod
    def bstack1llll11lll11_opy_(cls, response=None):
        os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ⇑")] = bstack11l1111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ⇒")
        os.environ[bstack11l1111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ⇓")] = bstack11l1111_opy_ (u"ࠨࡰࡸࡰࡱ࠭⇔")
        os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⇕")] = bstack11l1111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ⇖")
        cls.bstack1llll11l11ll_opy_(response, bstack11l1111_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦ⇗"))
        return [None, None, None]
    @classmethod
    def bstack1llll11ll111_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⇘")] = jwt
        os.environ[bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ⇙")] = build_hashed_id
    @classmethod
    def bstack1llll11l11ll_opy_(cls, response=None, product=bstack11l1111_opy_ (u"ࠢࠣ⇚")):
        if response == None or response.get(bstack11l1111_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨ⇛")) == None:
            logger.error(product + bstack11l1111_opy_ (u"ࠤࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠦ⇜"))
            return
        for error in response[bstack11l1111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪ⇝")]:
            bstack111l11ll1ll_opy_ = error[bstack11l1111_opy_ (u"ࠫࡰ࡫ࡹࠨ⇞")]
            error_message = error[bstack11l1111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⇟")]
            if error_message:
                if bstack111l11ll1ll_opy_ == bstack11l1111_opy_ (u"ࠨࡅࡓࡔࡒࡖࡤࡇࡃࡄࡇࡖࡗࡤࡊࡅࡏࡋࡈࡈࠧ⇠"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11l1111_opy_ (u"ࠢࡅࡣࡷࡥࠥࡻࡰ࡭ࡱࡤࡨࠥࡺ࡯ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࠣ⇡") + product + bstack11l1111_opy_ (u"ࠣࠢࡩࡥ࡮ࡲࡥࡥࠢࡧࡹࡪࠦࡴࡰࠢࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠨ⇢"))
    @classmethod
    def bstack1llll111ll11_opy_(cls):
        if cls.bstack11l111ll111_opy_ is not None:
            return
        cls.bstack11l111ll111_opy_ = bstack111l1ll11l1_opy_(cls.post_data)
        cls.bstack11l111ll111_opy_.start()
    @classmethod
    def bstack1l11llll_opy_(cls):
        if cls.bstack11l111ll111_opy_ is None:
            return
        cls.bstack11l111ll111_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1ll1l1l1_opy_, event_url=bstack11l1111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ⇣")):
        config = {
            bstack11l1111_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫ⇤"): cls.default_headers()
        }
        logger.debug(bstack11l1111_opy_ (u"ࠦࡵࡵࡳࡵࡡࡧࡥࡹࡧ࠺ࠡࡕࡨࡲࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡵࡱࠣࡸࡪࡹࡴࡩࡷࡥࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࡳࠡࡽࢀࠦ⇥").format(bstack11l1111_opy_ (u"ࠬ࠲ࠠࠨ⇦").join([event[bstack11l1111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇧")] for event in bstack1ll1l1l1_opy_])))
        response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"ࠧࡑࡑࡖࡘࠬ⇨"), cls.request_url(event_url), bstack1ll1l1l1_opy_, config)
        bstack1llll1l1111l_opy_ = response.json()
    @classmethod
    def bstack1l111111_opy_(cls, bstack1ll1l1l1_opy_, event_url=bstack11l1111_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ⇩")):
        logger.debug(bstack11l1111_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡡࡥࡦࠣࡨࡦࡺࡡࠡࡶࡲࠤࡧࡧࡴࡤࡪࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩ࠿ࠦࡻࡾࠤ⇪").format(bstack1ll1l1l1_opy_[bstack11l1111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇫")]))
        if not bstack11l1lll11l_opy_.bstack1llll111l1l1_opy_(bstack1ll1l1l1_opy_[bstack11l1111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇬")]):
            logger.debug(bstack11l1111_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡑࡳࡹࠦࡡࡥࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ⇭").format(bstack1ll1l1l1_opy_[bstack11l1111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇮")]))
            return
        bstack111l1lll1_opy_ = bstack11l1lll11l_opy_.bstack1llll11l1ll1_opy_(bstack1ll1l1l1_opy_[bstack11l1111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇯")], bstack1ll1l1l1_opy_.get(bstack11l1111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ⇰")))
        if bstack111l1lll1_opy_ != None:
            if bstack1ll1l1l1_opy_.get(bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⇱")) != None:
                bstack1ll1l1l1_opy_[bstack11l1111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ⇲")][bstack11l1111_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩ⇳")] = bstack111l1lll1_opy_
            else:
                bstack1ll1l1l1_opy_[bstack11l1111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ⇴")] = bstack111l1lll1_opy_
        if event_url == bstack11l1111_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬ⇵"):
            cls.bstack1llll111ll11_opy_()
            logger.debug(bstack11l1111_opy_ (u"ࠢࡴࡧࡱࡨࡤࡪࡡࡵࡣ࠽ࠤࡆࡪࡤࡪࡰࡪࠤࡩࡧࡴࡢࠢࡷࡳࠥࡨࡡࡵࡥ࡫ࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ⇶").format(bstack1ll1l1l1_opy_[bstack11l1111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇷")]))
            cls.bstack11l111ll111_opy_.add(bstack1ll1l1l1_opy_)
        elif event_url == bstack11l1111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ⇸"):
            cls.post_data([bstack1ll1l1l1_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack11lll11l_opy_(cls, logs):
        for log in logs:
            bstack1llll111l1ll_opy_ = {
                bstack11l1111_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ⇹"): bstack11l1111_opy_ (u"࡙ࠫࡋࡓࡕࡡࡏࡓࡌ࠭⇺"),
                bstack11l1111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⇻"): log[bstack11l1111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇼")],
                bstack11l1111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇽"): log[bstack11l1111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇾")],
                bstack11l1111_opy_ (u"ࠩ࡫ࡸࡹࡶ࡟ࡳࡧࡶࡴࡴࡴࡳࡦࠩ⇿"): {},
                bstack11l1111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ∀"): log[bstack11l1111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ∁")],
            }
            if bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ∂") in log:
                bstack1llll111l1ll_opy_[bstack11l1111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭∃")] = log[bstack11l1111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ∄")]
            elif bstack11l1111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ∅") in log:
                bstack1llll111l1ll_opy_[bstack11l1111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∆")] = log[bstack11l1111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ∇")]
            cls.bstack1l111111_opy_({
                bstack11l1111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ∈"): bstack11l1111_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ∉"),
                bstack11l1111_opy_ (u"࠭࡬ࡰࡩࡶࠫ∊"): [bstack1llll111l1ll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l1111_opy_(cls, steps):
        bstack1llll11ll1ll_opy_ = []
        for step in steps:
            bstack1llll1111ll1_opy_ = {
                bstack11l1111_opy_ (u"ࠧ࡬࡫ࡱࡨࠬ∋"): bstack11l1111_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡓࡕࡇࡓࠫ∌"),
                bstack11l1111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ∍"): step[bstack11l1111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ∎")],
                bstack11l1111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ∏"): step[bstack11l1111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ∐")],
                bstack11l1111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ∑"): step[bstack11l1111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ−")],
                bstack11l1111_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ∓"): step[bstack11l1111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ∔")]
            }
            if bstack11l1111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ∕") in step:
                bstack1llll1111ll1_opy_[bstack11l1111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ∖")] = step[bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ∗")]
            elif bstack11l1111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭∘") in step:
                bstack1llll1111ll1_opy_[bstack11l1111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ∙")] = step[bstack11l1111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ√")]
            bstack1llll11ll1ll_opy_.append(bstack1llll1111ll1_opy_)
        cls.bstack1l111111_opy_({
            bstack11l1111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭∛"): bstack11l1111_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ∜"),
            bstack11l1111_opy_ (u"ࠫࡱࡵࡧࡴࠩ∝"): bstack1llll11ll1ll_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack111l1lll1l_opy_, stage=STAGE.bstack1111ll111_opy_)
    def bstack1l11lllll_opy_(cls, screenshot):
        cls.bstack1l111111_opy_({
            bstack11l1111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ∞"): bstack11l1111_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ∟"),
            bstack11l1111_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ∠"): [{
                bstack11l1111_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭∡"): bstack11l1111_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࠫ∢"),
                bstack11l1111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭∣"): datetime.datetime.utcnow().isoformat() + bstack11l1111_opy_ (u"ࠫ࡟࠭∤"),
                bstack11l1111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭∥"): screenshot[bstack11l1111_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬ∦")],
                bstack11l1111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ∧"): screenshot[bstack11l1111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ∨")]
            }]
        }, event_url=bstack11l1111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ∩"))
    @classmethod
    @error_handler(class_method=True)
    def bstack11ll111lll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l111111_opy_({
            bstack11l1111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ∪"): bstack11l1111_opy_ (u"ࠫࡈࡈࡔࡔࡧࡶࡷ࡮ࡵ࡮ࡄࡴࡨࡥࡹ࡫ࡤࠨ∫"),
            bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ∬"): {
                bstack11l1111_opy_ (u"ࠨࡵࡶ࡫ࡧࠦ∭"): cls.current_test_uuid(),
                bstack11l1111_opy_ (u"ࠢࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸࠨ∮"): cls.bstack1l1l11l1_opy_(driver)
            }
        })
    @classmethod
    def bstack1ll1l11l_opy_(cls, event: str, bstack1ll1l1l1_opy_: bstack1l1ll11l_opy_):
        bstack1l111lll_opy_ = {
            bstack11l1111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ∯"): event,
            bstack1ll1l1l1_opy_.event_key(): bstack1ll1l1l1_opy_.bstack1l11lll1_opy_(event)
        }
        cls.bstack1l111111_opy_(bstack1l111lll_opy_)
        result = getattr(bstack1ll1l1l1_opy_, bstack11l1111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ∰"), None)
        if event == bstack11l1111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ∱"):
            threading.current_thread().bstackTestMeta = {bstack11l1111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ∲"): bstack11l1111_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭∳")}
        elif event == bstack11l1111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ∴"):
            threading.current_thread().bstackTestMeta = {bstack11l1111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ∵"): getattr(result, bstack11l1111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ∶"), bstack11l1111_opy_ (u"ࠩࠪ∷"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ∸"), None) is None or os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ∹")] == bstack11l1111_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ∺")) and (os.environ.get(bstack11l1111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ∻"), None) is None or os.environ[bstack11l1111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ∼")] == bstack11l1111_opy_ (u"ࠣࡰࡸࡰࡱࠨ∽")):
            return False
        return True
    @staticmethod
    def bstack1llll11l1l11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11l1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11l1111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ∾"): bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭∿"),
            bstack11l1111_opy_ (u"ࠫ࡝࠳ࡂࡔࡖࡄࡇࡐ࠳ࡔࡆࡕࡗࡓࡕ࡙ࠧ≀"): bstack11l1111_opy_ (u"ࠬࡺࡲࡶࡧࠪ≁")
        }
        if os.environ.get(bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ≂"), None):
            headers[bstack11l1111_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧ≃")] = bstack11l1111_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫ≄").format(os.environ[bstack11l1111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙ࠨ≅")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11l1111_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩ≆").format(bstack1llll111lll1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ≇"), None)
    @staticmethod
    def bstack1l1l11l1_opy_(driver):
        return {
            bstack111l11l11ll_opy_(): bstack1111l111ll1_opy_(driver)
        }
    @staticmethod
    def bstack1llll1111lll_opy_(exception_info, report):
        return [{bstack11l1111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ≈"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111111ll_opy_(typename):
        if bstack11l1111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤ≉") in typename:
            return bstack11l1111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣ≊")
        return bstack11l1111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤ≋")