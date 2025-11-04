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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll111l1l_opy_ import bstack1llll1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll111l1_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack1lllll11ll1_opy_,
    bstack1llll1ll11l_opy_,
)
from bstack_utils.helper import  bstack1llll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1ll1_opy_, bstack1lll1ll11ll_opy_, bstack1lll11l11ll_opy_, bstack1l1lllll11l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11llll1111_opy_ import bstack1llllll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111ll1_opy_ import bstack1lll1111l11_opy_
from bstack_utils.percy import bstack11l1lll111_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l11ll1111l_opy_(bstack1llll1l1ll1_opy_):
    def __init__(self, bstack11llll11lll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llll11lll_opy_ = bstack11llll11lll_opy_
        self.percy = bstack11l1lll111_opy_()
        self.bstack1l111ll11_opy_ = bstack1llllll11l_opy_()
        self.bstack11llll11ll1_opy_()
        bstack1lllll11111_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.bstack1llll1l1l1l_opy_, bstack1lllll11ll1_opy_.PRE), self.bstack11llll1l1ll_opy_)
        TestFramework.bstack1llllll11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll11l11ll_opy_.POST), self.bstack1lll1l1l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1l1lll_opy_(self, instance: bstack1llll1ll11l_opy_, driver: object):
        bstack1l11l1ll11l_opy_ = TestFramework.bstack1l11l1ll1l1_opy_(instance.context)
        for t in bstack1l11l1ll11l_opy_:
            bstack1lll1111l1l_opy_ = TestFramework.get_state(t, bstack1lll1111l11_opy_.bstack1llll111111_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111l1l_opy_) or instance == driver:
                return t
    def bstack11llll1l1ll_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll11111_opy_.bstack1l1ll1l11l1_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll11111_opy_.bstack1llll11ll1l_opy_, 0)
            bstack1ll11ll1lll_opy_ = self.bstack1l11l1l1lll_opy_(instance, driver)
            bstack11llll1lll1_opy_ = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1l1lllll1ll_opy_, None)
            if not bstack11llll1lll1_opy_:
                self.logger.debug(bstack11l1111_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡲࡦࡶࡸࡶࡳ࡯࡮ࡨࠢࡤࡷࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡩࡴࠢࡱࡳࡹࠦࡹࡦࡶࠣࡷࡹࡧࡲࡵࡧࡧࠦᕘ"))
                return
            driver_command = f.bstack1l1ll1ll1ll_opy_(*args)
            for command in bstack1111l1l11l_opy_:
                if command == driver_command:
                    self.bstack1lll11l1l1_opy_(driver, platform_index)
            bstack1l11ll111l_opy_ = self.percy.bstack1lll1ll111_opy_()
            if driver_command in bstack11ll11111l_opy_[bstack1l11ll111l_opy_]:
                self.bstack1l111ll11_opy_.bstack11l1llll11_opy_(bstack11llll1lll1_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡦࡴࡵࡳࡷࠨᕙ"), e)
    def bstack1lll1l1l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111111l1l1_opy_ import bstack1llll1l1111_opy_
        bstack1lll1111l1l_opy_ = f.get_state(instance, bstack1lll1111l11_opy_.bstack1llll111111_opy_, [])
        if not bstack1lll1111l1l_opy_:
            self.logger.debug(bstack11l1111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᕚ") + str(kwargs) + bstack11l1111_opy_ (u"ࠢࠣᕛ"))
            return
        if len(bstack1lll1111l1l_opy_) > 1:
            self.logger.debug(bstack11l1111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕜ") + str(kwargs) + bstack11l1111_opy_ (u"ࠤࠥᕝ"))
        bstack1lll111l111_opy_, bstack1lll1ll111l_opy_ = bstack1lll1111l1l_opy_[0]
        driver = bstack1lll111l111_opy_()
        if not driver:
            self.logger.debug(bstack11l1111_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᕞ") + str(kwargs) + bstack11l1111_opy_ (u"ࠦࠧᕟ"))
            return
        bstack11llll11l1l_opy_ = {
            TestFramework.bstack1l1lll11lll_opy_: bstack11l1111_opy_ (u"ࠧࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣᕠ"),
            TestFramework.bstack1lll11ll111_opy_: bstack11l1111_opy_ (u"ࠨࡴࡦࡵࡷࠤࡺࡻࡩࡥࠤᕡ"),
            TestFramework.bstack1l1lllll1ll_opy_: bstack11l1111_opy_ (u"ࠢࡵࡧࡶࡸࠥࡸࡥࡳࡷࡱࠤࡳࡧ࡭ࡦࠤᕢ")
        }
        bstack11llll1ll11_opy_ = { key: f.get_state(instance, key) for key in bstack11llll11l1l_opy_ }
        bstack11llll1l1l1_opy_ = [key for key, value in bstack11llll1ll11_opy_.items() if not value]
        if bstack11llll1l1l1_opy_:
            for key in bstack11llll1l1l1_opy_:
                self.logger.debug(bstack11l1111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠦᕣ") + str(key) + bstack11l1111_opy_ (u"ࠤࠥᕤ"))
            return
        platform_index = f.get_state(instance, bstack1lllll11111_opy_.bstack1llll11ll1l_opy_, 0)
        if self.bstack11llll11lll_opy_.percy_capture_mode == bstack11l1111_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᕥ"):
            bstack11l11l1l1_opy_ = bstack11llll1ll11_opy_.get(TestFramework.bstack1l1lllll1ll_opy_) + bstack11l1111_opy_ (u"ࠦ࠲ࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᕦ")
            bstack1l1llll111l_opy_ = bstack1llll1l1111_opy_.bstack1ll1111l111_opy_(EVENTS.bstack11llll1ll1l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11l11l1l1_opy_,
                bstack11l1l11ll1_opy_=bstack11llll1ll11_opy_[TestFramework.bstack1l1lll11lll_opy_],
                bstack1l1111ll1_opy_=bstack11llll1ll11_opy_[TestFramework.bstack1lll11ll111_opy_],
                bstack1l1l111l11_opy_=platform_index
            )
            bstack1llll1l1111_opy_.end(EVENTS.bstack11llll1ll1l_opy_.value, bstack1l1llll111l_opy_+bstack11l1111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᕧ"), bstack1l1llll111l_opy_+bstack11l1111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᕨ"), True, None, None, None, None, test_name=bstack11l11l1l1_opy_)
    def bstack1lll11l1l1_opy_(self, driver, platform_index):
        if self.bstack1l111ll11_opy_.bstack1ll1ll1lll_opy_() is True or self.bstack1l111ll11_opy_.capturing() is True:
            return
        self.bstack1l111ll11_opy_.bstack111l11llll_opy_()
        while not self.bstack1l111ll11_opy_.bstack1ll1ll1lll_opy_():
            bstack11llll1lll1_opy_ = self.bstack1l111ll11_opy_.bstack1l1l111l1_opy_()
            self.bstack1ll11l1l11_opy_(driver, bstack11llll1lll1_opy_, platform_index)
        self.bstack1l111ll11_opy_.bstack11l11l1l1l_opy_()
    def bstack1ll11l1l11_opy_(self, driver, bstack1llll1l1ll_opy_, platform_index, test=None):
        from bstack_utils.bstack111111l1l1_opy_ import bstack1llll1l1111_opy_
        bstack1l1llll111l_opy_ = bstack1llll1l1111_opy_.bstack1ll1111l111_opy_(EVENTS.bstack1l111llll1_opy_.value)
        if test != None:
            bstack11l1l11ll1_opy_ = getattr(test, bstack11l1111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᕩ"), None)
            bstack1l1111ll1_opy_ = getattr(test, bstack11l1111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᕪ"), None)
            PercySDK.screenshot(driver, bstack1llll1l1ll_opy_, bstack11l1l11ll1_opy_=bstack11l1l11ll1_opy_, bstack1l1111ll1_opy_=bstack1l1111ll1_opy_, bstack1l1l111l11_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1llll1l1ll_opy_)
        bstack1llll1l1111_opy_.end(EVENTS.bstack1l111llll1_opy_.value, bstack1l1llll111l_opy_+bstack11l1111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᕫ"), bstack1l1llll111l_opy_+bstack11l1111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᕬ"), True, None, None, None, None, test_name=bstack1llll1l1ll_opy_)
    def bstack11llll11ll1_opy_(self):
        os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩᕭ")] = str(self.bstack11llll11lll_opy_.success)
        os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩᕮ")] = str(self.bstack11llll11lll_opy_.percy_capture_mode)
        self.percy.bstack11llll1l11l_opy_(self.bstack11llll11lll_opy_.is_percy_auto_enabled)
        self.percy.bstack11llll1l111_opy_(self.bstack11llll11lll_opy_.percy_build_id)