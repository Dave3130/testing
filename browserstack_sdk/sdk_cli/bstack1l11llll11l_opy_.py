# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll1111_opy_ import bstack111111ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack111111111l_opy_,
    bstack111111lll1_opy_,
)
from bstack_utils.helper import  bstack1ll1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1lllll11ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1llll1111ll_opy_, bstack1lll1ll111l_opy_, bstack1ll11l111l1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11lll1l111_opy_ import bstack1l1ll1llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11lll1l_opy_
from bstack_utils.percy import bstack1l1l11l1l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l11lll1ll1_opy_(bstack111111ll11_opy_):
    def __init__(self, bstack11llllll11l_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llllll11l_opy_ = bstack11llllll11l_opy_
        self.percy = bstack1l1l11l1l_opy_()
        self.bstack1l1ll111l_opy_ = bstack1l1ll1llll_opy_()
        self.bstack11llllll1ll_opy_()
        bstack1lllll11ll1_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_, bstack111111111l_opy_.PRE), self.bstack11lllllllll_opy_)
        TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11llll_opy_(self, instance: bstack111111lll1_opy_, driver: object):
        bstack1l11l111l11_opy_ = TestFramework.bstack1l11ll111ll_opy_(instance.context)
        for t in bstack1l11l111l11_opy_:
            bstack1lll11llll1_opy_ = TestFramework.get_state(t, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11llll1_opy_) or instance == driver:
                return t
    def bstack11lllllllll_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll11ll1_opy_.bstack1l1lll1lll1_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll11ll1_opy_.bstack1lllll111ll_opy_, 0)
            bstack1ll11ll1lll_opy_ = self.bstack1l11l11llll_opy_(instance, driver)
            bstack11llllll1l1_opy_ = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1ll1l11l11l_opy_, None)
            if not bstack11llllll1l1_opy_:
                self.logger.debug(bstack1ll11_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡲࡦࡶࡸࡶࡳ࡯࡮ࡨࠢࡤࡷࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡩࡴࠢࡱࡳࡹࠦࡹࡦࡶࠣࡷࡹࡧࡲࡵࡧࡧࠦᔙ"))
                return
            driver_command = f.bstack1l1lll11ll1_opy_(*args)
            for command in bstack1l1111l111_opy_:
                if command == driver_command:
                    self.bstack111l1l1111_opy_(driver, platform_index)
            bstack1ll11ll1l_opy_ = self.percy.bstack11l1111l1l_opy_()
            if driver_command in bstack1ll1l1l111_opy_[bstack1ll11ll1l_opy_]:
                self.bstack1l1ll111l_opy_.bstack111lll1l1_opy_(bstack11llllll1l1_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡦࡴࡵࡳࡷࠨᔚ"), e)
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l111l1l_opy_ import bstack1llll1lllll_opy_
        bstack1lll11llll1_opy_ = f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1lll11llll1_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᔛ") + str(kwargs) + bstack1ll11_opy_ (u"ࠢࠣᔜ"))
            return
        if len(bstack1lll11llll1_opy_) > 1:
            self.logger.debug(bstack1ll11_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᔝ") + str(kwargs) + bstack1ll11_opy_ (u"ࠤࠥᔞ"))
        bstack1lll11l11l1_opy_, bstack1lll1lll1ll_opy_ = bstack1lll11llll1_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack1ll11_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᔟ") + str(kwargs) + bstack1ll11_opy_ (u"ࠦࠧᔠ"))
            return
        bstack1l11111111l_opy_ = {
            TestFramework.bstack1ll1ll11111_opy_: bstack1ll11_opy_ (u"ࠧࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣᔡ"),
            TestFramework.bstack1lll1l11ll1_opy_: bstack1ll11_opy_ (u"ࠨࡴࡦࡵࡷࠤࡺࡻࡩࡥࠤᔢ"),
            TestFramework.bstack1ll1l11l11l_opy_: bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࠥࡸࡥࡳࡷࡱࠤࡳࡧ࡭ࡦࠤᔣ")
        }
        bstack11llllllll1_opy_ = { key: f.get_state(instance, key) for key in bstack1l11111111l_opy_ }
        bstack1l111111111_opy_ = [key for key, value in bstack11llllllll1_opy_.items() if not value]
        if bstack1l111111111_opy_:
            for key in bstack1l111111111_opy_:
                self.logger.debug(bstack1ll11_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠦᔤ") + str(key) + bstack1ll11_opy_ (u"ࠤࠥᔥ"))
            return
        platform_index = f.get_state(instance, bstack1lllll11ll1_opy_.bstack1lllll111ll_opy_, 0)
        if self.bstack11llllll11l_opy_.percy_capture_mode == bstack1ll11_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᔦ"):
            bstack1ll111111l_opy_ = bstack11llllllll1_opy_.get(TestFramework.bstack1ll1l11l11l_opy_) + bstack1ll11_opy_ (u"ࠦ࠲ࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᔧ")
            bstack1ll1l1ll1l1_opy_ = bstack1llll1lllll_opy_.bstack1ll111lll1l_opy_(EVENTS.bstack11lllllll11_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1ll111111l_opy_,
                bstack1l1ll1111l_opy_=bstack11llllllll1_opy_[TestFramework.bstack1ll1ll11111_opy_],
                bstack1lll111l1l_opy_=bstack11llllllll1_opy_[TestFramework.bstack1lll1l11ll1_opy_],
                bstack1ll111llll_opy_=platform_index
            )
            bstack1llll1lllll_opy_.end(EVENTS.bstack11lllllll11_opy_.value, bstack1ll1l1ll1l1_opy_+bstack1ll11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᔨ"), bstack1ll1l1ll1l1_opy_+bstack1ll11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᔩ"), True, None, None, None, None, test_name=bstack1ll111111l_opy_)
    def bstack111l1l1111_opy_(self, driver, platform_index):
        if self.bstack1l1ll111l_opy_.bstack1ll1111l1l_opy_() is True or self.bstack1l1ll111l_opy_.capturing() is True:
            return
        self.bstack1l1ll111l_opy_.bstack11l1l1ll11_opy_()
        while not self.bstack1l1ll111l_opy_.bstack1ll1111l1l_opy_():
            bstack11llllll1l1_opy_ = self.bstack1l1ll111l_opy_.bstack11ll1l11l_opy_()
            self.bstack11l1l11ll1_opy_(driver, bstack11llllll1l1_opy_, platform_index)
        self.bstack1l1ll111l_opy_.bstack1ll1ll1ll_opy_()
    def bstack11l1l11ll1_opy_(self, driver, bstack1l1llllll1_opy_, platform_index, test=None):
        from bstack_utils.bstack11l111l1l_opy_ import bstack1llll1lllll_opy_
        bstack1ll1l1ll1l1_opy_ = bstack1llll1lllll_opy_.bstack1ll111lll1l_opy_(EVENTS.bstack1l11111l1_opy_.value)
        if test != None:
            bstack1l1ll1111l_opy_ = getattr(test, bstack1ll11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᔪ"), None)
            bstack1lll111l1l_opy_ = getattr(test, bstack1ll11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᔫ"), None)
            PercySDK.screenshot(driver, bstack1l1llllll1_opy_, bstack1l1ll1111l_opy_=bstack1l1ll1111l_opy_, bstack1lll111l1l_opy_=bstack1lll111l1l_opy_, bstack1ll111llll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l1llllll1_opy_)
        bstack1llll1lllll_opy_.end(EVENTS.bstack1l11111l1_opy_.value, bstack1ll1l1ll1l1_opy_+bstack1ll11_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᔬ"), bstack1ll1l1ll1l1_opy_+bstack1ll11_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᔭ"), True, None, None, None, None, test_name=bstack1l1llllll1_opy_)
    def bstack11llllll1ll_opy_(self):
        os.environ[bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩᔮ")] = str(self.bstack11llllll11l_opy_.success)
        os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩᔯ")] = str(self.bstack11llllll11l_opy_.percy_capture_mode)
        self.percy.bstack11lllllll1l_opy_(self.bstack11llllll11l_opy_.is_percy_auto_enabled)
        self.percy.bstack1l1111111l1_opy_(self.bstack11llllll11l_opy_.percy_build_id)