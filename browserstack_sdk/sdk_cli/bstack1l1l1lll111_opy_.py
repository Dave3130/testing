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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import (
    bstack1llll1l1ll1_opy_,
    bstack1llll11llll_opy_,
    bstack1llll111l1l_opy_,
)
from bstack_utils.helper import  bstack1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1ll111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l111l1_opy_, bstack1lll1l1l1ll_opy_, bstack1lll1ll1ll1_opy_, bstack1l1llll111l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l11llll1l_opy_ import bstack1l1l111l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1lll11111l1_opy_
from bstack_utils.percy import bstack1ll11l1ll_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l11lll11ll_opy_(bstack1lllll111l1_opy_):
    def __init__(self, bstack11llll11ll1_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llll11ll1_opy_ = bstack11llll11ll1_opy_
        self.percy = bstack1ll11l1ll_opy_()
        self.bstack111llllll1_opy_ = bstack1l1l111l11_opy_()
        self.bstack11llll1l1l1_opy_()
        bstack1llll1ll111_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.bstack1llll1lll11_opy_, bstack1llll11llll_opy_.PRE), self.bstack11llll1l11l_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.POST), self.bstack1lll1ll111l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11lll1_opy_(self, instance: bstack1llll111l1l_opy_, driver: object):
        bstack1l11l111ll1_opy_ = TestFramework.bstack1l11l11l1ll_opy_(instance.context)
        for t in bstack1l11l111ll1_opy_:
            bstack1lll1111111_opy_ = TestFramework.get_state(t, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111111_opy_) or instance == driver:
                return t
    def bstack11llll1l11l_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llll1ll111_opy_.bstack1l1lll11ll1_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1llll1ll111_opy_.bstack1llll1l11ll_opy_, 0)
            bstack1ll111l1l11_opy_ = self.bstack1l11l11lll1_opy_(instance, driver)
            bstack11llll11l1l_opy_ = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1ll111ll11l_opy_, None)
            if not bstack11llll11l1l_opy_:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡳࡧࡷࡹࡷࡴࡩ࡯ࡩࠣࡥࡸࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡪࡵࠣࡲࡴࡺࠠࡺࡧࡷࠤࡸࡺࡡࡳࡶࡨࡨࠧᕙ"))
                return
            driver_command = f.bstack1l1ll1lll1l_opy_(*args)
            for command in bstack111lllll11_opy_:
                if command == driver_command:
                    self.bstack1l1llll1l_opy_(driver, platform_index)
            bstack11l111l1l1_opy_ = self.percy.bstack11ll1l111l_opy_()
            if driver_command in bstack1111lll1ll_opy_[bstack11l111l1l1_opy_]:
                self.bstack111llllll1_opy_.bstack111l11ll1_opy_(bstack11llll11l1l_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡧࡵࡶࡴࡸࠢᕚ"), e)
    def bstack1lll1ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
        bstack1lll1111111_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll1111111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᕛ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠣࠤᕜ"))
            return
        if len(bstack1lll1111111_opy_) > 1:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᕝ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠥࠦᕞ"))
        bstack1lll1111lll_opy_, bstack1llll111l11_opy_ = bstack1lll1111111_opy_[0]
        driver = bstack1lll1111lll_opy_()
        if not driver:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᕟ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠧࠨᕠ"))
            return
        bstack11llll11lll_opy_ = {
            TestFramework.bstack1ll11ll11l1_opy_: bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᕡ"),
            TestFramework.bstack1lll11llll1_opy_: bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࠥࡻࡵࡪࡦࠥᕢ"),
            TestFramework.bstack1ll111ll11l_opy_: bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࠦࡲࡦࡴࡸࡲࠥࡴࡡ࡮ࡧࠥᕣ")
        }
        bstack11llll1l1ll_opy_ = { key: f.get_state(instance, key) for key in bstack11llll11lll_opy_ }
        bstack11llll1ll11_opy_ = [key for key, value in bstack11llll1l1ll_opy_.items() if not value]
        if bstack11llll1ll11_opy_:
            for key in bstack11llll1ll11_opy_:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠧᕤ") + str(key) + bstack11ll1ll_opy_ (u"ࠥࠦᕥ"))
            return
        platform_index = f.get_state(instance, bstack1llll1ll111_opy_.bstack1llll1l11ll_opy_, 0)
        if self.bstack11llll11ll1_opy_.percy_capture_mode == bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᕦ"):
            bstack1l11111l1_opy_ = bstack11llll1l1ll_opy_.get(TestFramework.bstack1ll111ll11l_opy_) + bstack11ll1ll_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣᕧ")
            bstack1l1lll1l1ll_opy_ = bstack1llll11l11l_opy_.bstack1l1lll1l111_opy_(EVENTS.bstack11llll1l111_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l11111l1_opy_,
                bstack1ll1ll1l1l_opy_=bstack11llll1l1ll_opy_[TestFramework.bstack1ll11ll11l1_opy_],
                bstack1l1l1ll11l_opy_=bstack11llll1l1ll_opy_[TestFramework.bstack1lll11llll1_opy_],
                bstack111lll1ll_opy_=platform_index
            )
            bstack1llll11l11l_opy_.end(EVENTS.bstack11llll1l111_opy_.value, bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᕨ"), bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᕩ"), True, None, None, None, None, test_name=bstack1l11111l1_opy_)
    def bstack1l1llll1l_opy_(self, driver, platform_index):
        if self.bstack111llllll1_opy_.bstack1ll1l1l1l1_opy_() is True or self.bstack111llllll1_opy_.capturing() is True:
            return
        self.bstack111llllll1_opy_.bstack11111ll11l_opy_()
        while not self.bstack111llllll1_opy_.bstack1ll1l1l1l1_opy_():
            bstack11llll11l1l_opy_ = self.bstack111llllll1_opy_.bstack11l11l1l1_opy_()
            self.bstack11ll1ll1l_opy_(driver, bstack11llll11l1l_opy_, platform_index)
        self.bstack111llllll1_opy_.bstack1ll11ll11_opy_()
    def bstack11ll1ll1l_opy_(self, driver, bstack111l1111l1_opy_, platform_index, test=None):
        from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
        bstack1l1lll1l1ll_opy_ = bstack1llll11l11l_opy_.bstack1l1lll1l111_opy_(EVENTS.bstack1111ll1ll_opy_.value)
        if test != None:
            bstack1ll1ll1l1l_opy_ = getattr(test, bstack11ll1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᕪ"), None)
            bstack1l1l1ll11l_opy_ = getattr(test, bstack11ll1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᕫ"), None)
            PercySDK.screenshot(driver, bstack111l1111l1_opy_, bstack1ll1ll1l1l_opy_=bstack1ll1ll1l1l_opy_, bstack1l1l1ll11l_opy_=bstack1l1l1ll11l_opy_, bstack111lll1ll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack111l1111l1_opy_)
        bstack1llll11l11l_opy_.end(EVENTS.bstack1111ll1ll_opy_.value, bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᕬ"), bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᕭ"), True, None, None, None, None, test_name=bstack111l1111l1_opy_)
    def bstack11llll1l1l1_opy_(self):
        os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪᕮ")] = str(self.bstack11llll11ll1_opy_.success)
        os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪᕯ")] = str(self.bstack11llll11ll1_opy_.percy_capture_mode)
        self.percy.bstack11llll1ll1l_opy_(self.bstack11llll11ll1_opy_.is_percy_auto_enabled)
        self.percy.bstack11llll1lll1_opy_(self.bstack11llll11ll1_opy_.percy_build_id)