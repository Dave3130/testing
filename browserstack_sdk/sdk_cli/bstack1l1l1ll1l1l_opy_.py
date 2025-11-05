# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
    bstack1lllllll11l_opy_,
)
from bstack_utils.helper import  bstack1ll111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1llll111111_opy_, bstack1lll11lll11_opy_, bstack1l1lllll1ll_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1ll1l111l1_opy_ import bstack11lllll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1lll11l1111_opy_
from bstack_utils.percy import bstack11l11lll11_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l1l1l1ll_opy_(bstack1lllllll1l1_opy_):
    def __init__(self, bstack11llll1l1ll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llll1l1ll_opy_ = bstack11llll1l1ll_opy_
        self.percy = bstack11l11lll11_opy_()
        self.bstack1ll11lll1l_opy_ = bstack11lllll1ll_opy_()
        self.bstack11llll1l11l_opy_()
        bstack1llllll1ll1_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.PRE), self.bstack11llll1l1l1_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.POST), self.bstack1lll1lll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l111lll1l1_opy_(self, instance: bstack1lllllll11l_opy_, driver: object):
        bstack1l111lll11l_opy_ = TestFramework.bstack1l11l1l1111_opy_(instance.context)
        for t in bstack1l111lll11l_opy_:
            bstack1lll111l1l1_opy_ = TestFramework.get_state(t, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll111l1l1_opy_) or instance == driver:
                return t
    def bstack11llll1l1l1_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llllll1ll1_opy_.bstack1l1lll1111l_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_, 0)
            bstack1ll1l11llll_opy_ = self.bstack1l111lll1l1_opy_(instance, driver)
            bstack11llll1ll1l_opy_ = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1ll1l1l11ll_opy_, None)
            if not bstack11llll1ll1l_opy_:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡴࡨࡸࡺࡸ࡮ࡪࡰࡪࠤࡦࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡ࡫ࡶࠤࡳࡵࡴࠡࡻࡨࡸࠥࡹࡴࡢࡴࡷࡩࡩࠨᔾ"))
                return
            driver_command = f.bstack1l1ll1ll1l1_opy_(*args)
            for command in bstack1111ll11ll_opy_:
                if command == driver_command:
                    self.bstack1111l1l1l_opy_(driver, platform_index)
            bstack1l1ll1l1l_opy_ = self.percy.bstack11lllll11_opy_()
            if driver_command in bstack11111l1lll_opy_[bstack1l1ll1l1l_opy_]:
                self.bstack1ll11lll1l_opy_.bstack1l11llll1_opy_(bstack11llll1ll1l_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡨࡶࡷࡵࡲࠣᔿ"), e)
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
        bstack1lll111l1l1_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, [])
        if not bstack1lll111l1l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕀ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠤࠥᕁ"))
            return
        if len(bstack1lll111l1l1_opy_) > 1:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᕂ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠦࠧᕃ"))
        bstack1lll111l1ll_opy_, bstack1lll11llll1_opy_ = bstack1lll111l1l1_opy_[0]
        driver = bstack1lll111l1ll_opy_()
        if not driver:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᕄ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠨࠢᕅ"))
            return
        bstack11lllll111l_opy_ = {
            TestFramework.bstack1l1lll1l1ll_opy_: bstack1lll11l_opy_ (u"ࠢࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᕆ"),
            TestFramework.bstack1lll11ll11l_opy_: bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࠦࡵࡶ࡫ࡧࠦᕇ"),
            TestFramework.bstack1ll1l1l11ll_opy_: bstack1lll11l_opy_ (u"ࠤࡷࡩࡸࡺࠠࡳࡧࡵࡹࡳࠦ࡮ࡢ࡯ࡨࠦᕈ")
        }
        bstack11llll1lll1_opy_ = { key: f.get_state(instance, key) for key in bstack11lllll111l_opy_ }
        bstack11lllll11l1_opy_ = [key for key, value in bstack11llll1lll1_opy_.items() if not value]
        if bstack11lllll11l1_opy_:
            for key in bstack11lllll11l1_opy_:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࠨᕉ") + str(key) + bstack1lll11l_opy_ (u"ࠦࠧᕊ"))
            return
        platform_index = f.get_state(instance, bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_, 0)
        if self.bstack11llll1l1ll_opy_.percy_capture_mode == bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᕋ"):
            bstack1l11lll11_opy_ = bstack11llll1lll1_opy_.get(TestFramework.bstack1ll1l1l11ll_opy_) + bstack1lll11l_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᕌ")
            bstack1ll111111l1_opy_ = bstack1llll1l1l1l_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack11lllll1111_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l11lll11_opy_,
                bstack1ll111111l_opy_=bstack11llll1lll1_opy_[TestFramework.bstack1l1lll1l1ll_opy_],
                bstack11l1llll1l_opy_=bstack11llll1lll1_opy_[TestFramework.bstack1lll11ll11l_opy_],
                bstack111l1lll1l_opy_=platform_index
            )
            bstack1llll1l1l1l_opy_.end(EVENTS.bstack11lllll1111_opy_.value, bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᕍ"), bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᕎ"), True, None, None, None, None, test_name=bstack1l11lll11_opy_)
    def bstack1111l1l1l_opy_(self, driver, platform_index):
        if self.bstack1ll11lll1l_opy_.bstack1ll11l11l1_opy_() is True or self.bstack1ll11lll1l_opy_.capturing() is True:
            return
        self.bstack1ll11lll1l_opy_.bstack1ll11l111l_opy_()
        while not self.bstack1ll11lll1l_opy_.bstack1ll11l11l1_opy_():
            bstack11llll1ll1l_opy_ = self.bstack1ll11lll1l_opy_.bstack1lll1111l1_opy_()
            self.bstack11ll111l11_opy_(driver, bstack11llll1ll1l_opy_, platform_index)
        self.bstack1ll11lll1l_opy_.bstack11lll1l11l_opy_()
    def bstack11ll111l11_opy_(self, driver, bstack11111ll1ll_opy_, platform_index, test=None):
        from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
        bstack1ll111111l1_opy_ = bstack1llll1l1l1l_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack1l1l11l11l_opy_.value)
        if test != None:
            bstack1ll111111l_opy_ = getattr(test, bstack1lll11l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᕏ"), None)
            bstack11l1llll1l_opy_ = getattr(test, bstack1lll11l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᕐ"), None)
            PercySDK.screenshot(driver, bstack11111ll1ll_opy_, bstack1ll111111l_opy_=bstack1ll111111l_opy_, bstack11l1llll1l_opy_=bstack11l1llll1l_opy_, bstack111l1lll1l_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11111ll1ll_opy_)
        bstack1llll1l1l1l_opy_.end(EVENTS.bstack1l1l11l11l_opy_.value, bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕑ"), bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕒ"), True, None, None, None, None, test_name=bstack11111ll1ll_opy_)
    def bstack11llll1l11l_opy_(self):
        os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᕓ")] = str(self.bstack11llll1l1ll_opy_.success)
        os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᕔ")] = str(self.bstack11llll1l1ll_opy_.percy_capture_mode)
        self.percy.bstack11llll1llll_opy_(self.bstack11llll1l1ll_opy_.is_percy_auto_enabled)
        self.percy.bstack11llll1ll11_opy_(self.bstack11llll1l1ll_opy_.percy_build_id)