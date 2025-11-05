# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1llll111ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1111_opy_,
    bstack1llll111l1l_opy_,
)
from bstack_utils.helper import  bstack1lll1lll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll111ll_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1l1ll1l_opy_, bstack1lll1ll1l1l_opy_, bstack1ll111lll1l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l1l1ll1l_opy_ import bstack111l1111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111111l_opy_ import bstack1ll1lllll1l_opy_
from bstack_utils.percy import bstack111ll1lll1_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l1l11l1l_opy_(bstack1llll111ll1_opy_):
    def __init__(self, bstack11llll11l1l_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llll11l1l_opy_ = bstack11llll11l1l_opy_
        self.percy = bstack111ll1lll1_opy_()
        self.bstack11l1l1111_opy_ = bstack111l1111l1_opy_()
        self.bstack11llll1lll1_opy_()
        bstack1lllll1111l_opy_.bstack1llll11ll11_opy_((bstack1lllllll1l1_opy_.bstack1lllll1llll_opy_, bstack1llllll1111_opy_.PRE), self.bstack11llll11lll_opy_)
        TestFramework.bstack1llll11ll11_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1ll1l1l_opy_.POST), self.bstack1lll1ll1ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11l1l1_opy_(self, instance: bstack1llll111l1l_opy_, driver: object):
        bstack1l111lll1l1_opy_ = TestFramework.bstack1l11l11llll_opy_(instance.context)
        for t in bstack1l111lll1l1_opy_:
            bstack1lll11111l1_opy_ = TestFramework.get_state(t, bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11111l1_opy_) or instance == driver:
                return t
    def bstack11llll11lll_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll1111l_opy_.bstack1l1ll1l1lll_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll1111l_opy_.bstack1lllll1ll11_opy_, 0)
            bstack1l1llll1ll1_opy_ = self.bstack1l11l11l1l1_opy_(instance, driver)
            bstack11llll1ll11_opy_ = TestFramework.get_state(bstack1l1llll1ll1_opy_, TestFramework.bstack1ll111ll1l1_opy_, None)
            if not bstack11llll1ll11_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡲࡦࡶࡸࡶࡳ࡯࡮ࡨࠢࡤࡷࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡩࡴࠢࡱࡳࡹࠦࡹࡦࡶࠣࡷࡹࡧࡲࡵࡧࡧࠦᕘ"))
                return
            driver_command = f.bstack1l1ll1lll1l_opy_(*args)
            for command in bstack1ll1ll111l_opy_:
                if command == driver_command:
                    self.bstack11lll1l1l_opy_(driver, platform_index)
            bstack11lll1ll1_opy_ = self.percy.bstack1l1l1l1l1_opy_()
            if driver_command in bstack1lll111l11_opy_[bstack11lll1ll1_opy_]:
                self.bstack11l1l1111_opy_.bstack11l1ll1lll_opy_(bstack11llll1ll11_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡦࡴࡵࡳࡷࠨᕙ"), e)
    def bstack1lll1ll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1ll11111ll_opy_ import bstack1llll1ll1l1_opy_
        bstack1lll11111l1_opy_ = f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_, [])
        if not bstack1lll11111l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᕚ") + str(kwargs) + bstack11111_opy_ (u"ࠢࠣᕛ"))
            return
        if len(bstack1lll11111l1_opy_) > 1:
            self.logger.debug(bstack11111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕜ") + str(kwargs) + bstack11111_opy_ (u"ࠤࠥᕝ"))
        bstack1lll111l111_opy_, bstack1lll1lll111_opy_ = bstack1lll11111l1_opy_[0]
        driver = bstack1lll111l111_opy_()
        if not driver:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᕞ") + str(kwargs) + bstack11111_opy_ (u"ࠦࠧᕟ"))
            return
        bstack11llll1ll1l_opy_ = {
            TestFramework.bstack1ll1l11l11l_opy_: bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣᕠ"),
            TestFramework.bstack1lll1lll1ll_opy_: bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࠤࡺࡻࡩࡥࠤᕡ"),
            TestFramework.bstack1ll111ll1l1_opy_: bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࠥࡸࡥࡳࡷࡱࠤࡳࡧ࡭ࡦࠤᕢ")
        }
        bstack11llll1l1l1_opy_ = { key: f.get_state(instance, key) for key in bstack11llll1ll1l_opy_ }
        bstack11llll1l1ll_opy_ = [key for key, value in bstack11llll1l1l1_opy_.items() if not value]
        if bstack11llll1l1ll_opy_:
            for key in bstack11llll1l1ll_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠦᕣ") + str(key) + bstack11111_opy_ (u"ࠤࠥᕤ"))
            return
        platform_index = f.get_state(instance, bstack1lllll1111l_opy_.bstack1lllll1ll11_opy_, 0)
        if self.bstack11llll11l1l_opy_.percy_capture_mode == bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᕥ"):
            bstack1l1111ll1_opy_ = bstack11llll1l1l1_opy_.get(TestFramework.bstack1ll111ll1l1_opy_) + bstack11111_opy_ (u"ࠦ࠲ࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᕦ")
            bstack1ll11llll1l_opy_ = bstack1llll1ll1l1_opy_.bstack1ll1111lll1_opy_(EVENTS.bstack11llll1l11l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l1111ll1_opy_,
                bstack1l1lll11l1_opy_=bstack11llll1l1l1_opy_[TestFramework.bstack1ll1l11l11l_opy_],
                bstack11l1ll1l11_opy_=bstack11llll1l1l1_opy_[TestFramework.bstack1lll1lll1ll_opy_],
                bstack1ll11l111l_opy_=platform_index
            )
            bstack1llll1ll1l1_opy_.end(EVENTS.bstack11llll1l11l_opy_.value, bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᕧ"), bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᕨ"), True, None, None, None, None, test_name=bstack1l1111ll1_opy_)
    def bstack11lll1l1l_opy_(self, driver, platform_index):
        if self.bstack11l1l1111_opy_.bstack1ll111llll_opy_() is True or self.bstack11l1l1111_opy_.capturing() is True:
            return
        self.bstack11l1l1111_opy_.bstack1111llll1l_opy_()
        while not self.bstack11l1l1111_opy_.bstack1ll111llll_opy_():
            bstack11llll1ll11_opy_ = self.bstack11l1l1111_opy_.bstack11l1l1l1l_opy_()
            self.bstack11l1lllll1_opy_(driver, bstack11llll1ll11_opy_, platform_index)
        self.bstack11l1l1111_opy_.bstack11l1llll1l_opy_()
    def bstack11l1lllll1_opy_(self, driver, bstack1lll1l1l11_opy_, platform_index, test=None):
        from bstack_utils.bstack1ll11111ll_opy_ import bstack1llll1ll1l1_opy_
        bstack1ll11llll1l_opy_ = bstack1llll1ll1l1_opy_.bstack1ll1111lll1_opy_(EVENTS.bstack1l1l111l11_opy_.value)
        if test != None:
            bstack1l1lll11l1_opy_ = getattr(test, bstack11111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᕩ"), None)
            bstack11l1ll1l11_opy_ = getattr(test, bstack11111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᕪ"), None)
            PercySDK.screenshot(driver, bstack1lll1l1l11_opy_, bstack1l1lll11l1_opy_=bstack1l1lll11l1_opy_, bstack11l1ll1l11_opy_=bstack11l1ll1l11_opy_, bstack1ll11l111l_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1lll1l1l11_opy_)
        bstack1llll1ll1l1_opy_.end(EVENTS.bstack1l1l111l11_opy_.value, bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᕫ"), bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᕬ"), True, None, None, None, None, test_name=bstack1lll1l1l11_opy_)
    def bstack11llll1lll1_opy_(self):
        os.environ[bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩᕭ")] = str(self.bstack11llll11l1l_opy_.success)
        os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩᕮ")] = str(self.bstack11llll11l1l_opy_.percy_capture_mode)
        self.percy.bstack11llll1l111_opy_(self.bstack11llll11l1l_opy_.is_percy_auto_enabled)
        self.percy.bstack11llll11ll1_opy_(self.bstack11llll11l1l_opy_.percy_build_id)