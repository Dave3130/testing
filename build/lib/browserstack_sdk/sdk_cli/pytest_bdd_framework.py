# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll1lll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack111l1lll11_opy_ import bstack1l1llll1lll_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll11ll_opy_,
    bstack1lll1llll11_opy_,
    bstack1lll1lll11l_opy_,
    bstack1l1llllll1l_opy_,
    bstack1ll11ll1ll1_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l1lllll_opy_
from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll11l1l111_opy_ import bstack1ll1111ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll11lll1l_opy_ import bstack1lll11llll1_opy_
bstack1ll1l111ll1_opy_ = bstack1ll1l1lllll_opy_()
bstack1ll1l11ll11_opy_ = bstack1l1lll1_opy_ (u"࡚ࠦࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠰ࠦᇴ")
bstack1ll11ll1lll_opy_ = bstack1l1lll1_opy_ (u"ࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠣᇵ")
bstack1ll1111lll1_opy_ = bstack1l1lll1_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠧᇶ")
bstack1ll1l1ll11l_opy_ = 1.0
_1ll11l11ll1_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll11llllll_opy_ = bstack1l1lll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᇷ")
    bstack1ll11lll1ll_opy_ = bstack1l1lll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࠨᇸ")
    bstack1ll11ll1111_opy_ = bstack1l1lll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᇹ")
    bstack1ll111l1lll_opy_ = bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࠧᇺ")
    bstack1ll1111l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᇻ")
    bstack1ll1l1ll111_opy_: bool
    bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_  = None
    bstack1ll1l1l1lll_opy_ = [
        bstack1lll1ll11ll_opy_.BEFORE_ALL,
        bstack1lll1ll11ll_opy_.AFTER_ALL,
        bstack1lll1ll11ll_opy_.BEFORE_EACH,
        bstack1lll1ll11ll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll1ll11111_opy_: Dict[str, str],
        bstack1ll1111l1l1_opy_: List[str]=[bstack1l1lll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᇼ")],
        bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_ = None,
        bstack1lllll1ll11_opy_=None
    ):
        super().__init__(bstack1ll1111l1l1_opy_, bstack1ll1ll11111_opy_, bstack1lll11lll1l_opy_)
        self.bstack1ll1l1ll111_opy_ = any(bstack1l1lll1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᇽ") in item.lower() for item in bstack1ll1111l1l1_opy_)
        self.bstack1lllll1ll11_opy_ = bstack1lllll1ll11_opy_
    def track_event(
        self,
        context: bstack1l1llllll1l_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll11ll_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1l1l1lll_opy_:
            bstack1l1llll1lll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll11ll_opy_.NONE:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࠣᇾ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠣࠤᇿ"))
            return
        if not self.bstack1ll1l1ll111_opy_:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠿ࠥሀ") + str(str(self.bstack1ll1111l1l1_opy_)) + bstack1l1lll1_opy_ (u"ࠥࠦሁ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨሂ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠧࠨሃ"))
            return
        instance = self.__1ll1l1lll11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡡࡳࡩࡶࡁࠧሄ") + str(args) + bstack1l1lll1_opy_ (u"ࠢࠣህ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1l1lll_opy_ and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1l11l111_opy_ = bstack1llll1ll11l_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack111ll1l1l_opy_.value)
                name = str(EVENTS.bstack111ll1l1l_opy_.name)+bstack1l1lll1_opy_ (u"ࠣ࠼ࠥሆ")+str(test_framework_state.name)
                TestFramework.bstack1ll11ll1l11_opy_(instance, name, bstack1ll1l11l111_opy_)
        except Exception as e:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶࠥࡶࡲࡦ࠼ࠣࡿࢂࠨሇ").format(e))
        try:
            if test_framework_state == bstack1lll1ll11ll_opy_.TEST:
                if not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1ll1l1l1l1l_opy_) and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll1l111lll_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡰࡴࡧࡤࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥለ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠦࠧሉ"))
                if test_hook_state == bstack1lll1lll11l_opy_.PRE and not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1ll11111111_opy_):
                    TestFramework.bstack1llll1lllll_opy_(instance, TestFramework.bstack1ll11111111_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll1111l11l_opy_(instance, args)
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡴࡶࡤࡶࡹࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥሊ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠨࠢላ"))
                elif test_hook_state == bstack1lll1lll11l_opy_.POST and not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1ll111111ll_opy_):
                    TestFramework.bstack1llll1lllll_opy_(instance, TestFramework.bstack1ll111111ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡨࡲࡩࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥሌ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠣࠤል"))
            elif test_framework_state == bstack1lll1ll11ll_opy_.STEP:
                if test_hook_state == bstack1lll1lll11l_opy_.PRE:
                    PytestBDDFramework.__1ll11l11l1l_opy_(instance, args)
                elif test_hook_state == bstack1lll1lll11l_opy_.POST:
                    PytestBDDFramework.__1ll111ll11l_opy_(instance, args)
            elif test_framework_state == bstack1lll1ll11ll_opy_.LOG and test_hook_state == bstack1lll1lll11l_opy_.POST:
                PytestBDDFramework.__1l1lllll1l1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll11ll_opy_.LOG_REPORT and test_hook_state == bstack1lll1lll11l_opy_.POST:
                self.__1ll1l11111l_opy_(instance, *args)
                self.__1ll1l111111_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1l1l1lll_opy_:
                self.__1l1lllll111_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥሎ") + str(instance.ref()) + bstack1l1lll1_opy_ (u"ࠥࠦሏ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll111l1l1l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1l1lll_opy_ and test_hook_state == bstack1lll1lll11l_opy_.POST:
                name = str(EVENTS.bstack111ll1l1l_opy_.name)+bstack1l1lll1_opy_ (u"ࠦ࠿ࠨሐ")+str(test_framework_state.name)
                bstack1ll1l11l111_opy_ = TestFramework.bstack1ll1l11llll_opy_(instance, name)
                bstack1llll1ll11l_opy_.end(EVENTS.bstack111ll1l1l_opy_.value, bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧሑ"), bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦሒ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢሓ").format(e))
    def bstack1ll11llll11_opy_(self):
        return self.bstack1ll1l1ll111_opy_
    def __1ll11l11l11_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1lll1_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧሔ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l1l1l11_opy_(rep, [bstack1l1lll1_opy_ (u"ࠤࡺ࡬ࡪࡴࠢሕ"), bstack1l1lll1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦሖ"), bstack1l1lll1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦሗ"), bstack1l1lll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧመ"), bstack1l1lll1_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠢሙ"), bstack1l1lll1_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨሚ")])
        return None
    def __1ll1l11111l_opy_(self, instance: bstack1lll1llll11_opy_, *args):
        result = self.__1ll11l11l11_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l1111_opy_ = None
        if result.get(bstack1l1lll1_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤማ"), None) == bstack1l1lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤሜ") and len(args) > 1 and getattr(args[1], bstack1l1lll1_opy_ (u"ࠥࡩࡽࡩࡩ࡯ࡨࡲࠦም"), None) is not None:
            failure = [{bstack1l1lll1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧሞ"): [args[1].excinfo.exconly(), result.get(bstack1l1lll1_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦሟ"), None)]}]
            bstack11111l1111_opy_ = bstack1l1lll1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢሠ") if bstack1l1lll1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥሡ") in getattr(args[1].excinfo, bstack1l1lll1_opy_ (u"ࠣࡶࡼࡴࡪࡴࡡ࡮ࡧࠥሢ"), bstack1l1lll1_opy_ (u"ࠤࠥሣ")) else bstack1l1lll1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦሤ")
        bstack1ll111l111l_opy_ = result.get(bstack1l1lll1_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧሥ"), TestFramework.bstack1ll11l1l11l_opy_)
        if bstack1ll111l111l_opy_ != TestFramework.bstack1ll11l1l11l_opy_:
            TestFramework.bstack1llll1lllll_opy_(instance, TestFramework.bstack1ll11l1l1l1_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l111l11_opy_(instance, {
            TestFramework.bstack1lll1ll111l_opy_: failure,
            TestFramework.bstack1ll1111llll_opy_: bstack11111l1111_opy_,
            TestFramework.bstack1lll1l11111_opy_: bstack1ll111l111l_opy_,
        })
    def __1ll1l1lll11_opy_(
        self,
        context: bstack1l1llllll1l_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll11ll_opy_.SETUP_FIXTURE:
            instance = self.__1ll11111lll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11l11111_opy_ bstack1l1lllll11l_opy_ this to be bstack1l1lll1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧሦ")
            if test_framework_state == bstack1lll1ll11ll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l11l1l1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll11ll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1lll1_opy_ (u"ࠨ࡮ࡰࡦࡨࠦሧ"), None), bstack1l1lll1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢረ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1lll1_opy_ (u"ࠣࡰࡲࡨࡪࠨሩ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1l1lll1_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤሪ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111lllll_opy_(target) if target else None
        return instance
    def __1l1lllll111_opy_(
        self,
        instance: bstack1lll1llll11_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l1ll1ll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11lll1ll_opy_, {})
        if not key in bstack1ll1l1ll1ll_opy_:
            bstack1ll1l1ll1ll_opy_[key] = []
        bstack1l1llllll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11ll1111_opy_, {})
        if not key in bstack1l1llllll11_opy_:
            bstack1l1llllll11_opy_[key] = []
        bstack1ll1l11l1ll_opy_ = {
            PytestBDDFramework.bstack1ll11lll1ll_opy_: bstack1ll1l1ll1ll_opy_,
            PytestBDDFramework.bstack1ll11ll1111_opy_: bstack1l1llllll11_opy_,
        }
        if test_hook_state == bstack1lll1lll11l_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1l1lll1_opy_ (u"ࠥ࡯ࡪࡿࠢራ"): key,
                TestFramework.bstack1ll11l111ll_opy_: uuid4().__str__(),
                TestFramework.bstack1l1lllllll1_opy_: TestFramework.bstack1ll11lllll1_opy_,
                TestFramework.bstack1ll11lll11l_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1111111l_opy_: [],
                TestFramework.bstack1ll11111l11_opy_: hook_name,
                TestFramework.bstack1ll1l11l11l_opy_: bstack1ll1111ll1l_opy_.bstack1ll1l1l1ll1_opy_()
            }
            bstack1ll1l1ll1ll_opy_[key].append(hook)
            bstack1ll1l11l1ll_opy_[PytestBDDFramework.bstack1ll111l1lll_opy_] = key
        elif test_hook_state == bstack1lll1lll11l_opy_.POST:
            bstack1ll111l11l1_opy_ = bstack1ll1l1ll1ll_opy_.get(key, [])
            hook = bstack1ll111l11l1_opy_.pop() if bstack1ll111l11l1_opy_ else None
            if hook:
                result = self.__1ll11l11l11_opy_(*args)
                if result:
                    bstack1ll1l1111l1_opy_ = result.get(bstack1l1lll1_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧሬ"), TestFramework.bstack1ll11lllll1_opy_)
                    if bstack1ll1l1111l1_opy_ != TestFramework.bstack1ll11lllll1_opy_:
                        hook[TestFramework.bstack1l1lllllll1_opy_] = bstack1ll1l1111l1_opy_
                hook[TestFramework.bstack1ll11l1ll11_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l11l11l_opy_] = bstack1ll1111ll1l_opy_.bstack1ll1l1l1ll1_opy_()
                self.bstack1ll11llll1l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11lll111_opy_, [])
                self.bstack1ll111l1l11_opy_(instance, logs)
                bstack1l1llllll11_opy_[key].append(hook)
                bstack1ll1l11l1ll_opy_[PytestBDDFramework.bstack1ll1111l1ll_opy_] = key
        TestFramework.bstack1ll1l111l11_opy_(instance, bstack1ll1l11l1ll_opy_)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡭ࡵ࡯࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡱࡥࡺࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪ࠽ࡼࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡾࠢ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡀࠦር") + str(bstack1l1llllll11_opy_) + bstack1l1lll1_opy_ (u"ࠨࠢሮ"))
    def __1ll11111lll_opy_(
        self,
        context: bstack1l1llllll1l_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l1l1l11_opy_(args[0], [bstack1l1lll1_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨሯ"), bstack1l1lll1_opy_ (u"ࠣࡣࡵ࡫ࡳࡧ࡭ࡦࠤሰ"), bstack1l1lll1_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤሱ"), bstack1l1lll1_opy_ (u"ࠥ࡭ࡩࡹࠢሲ"), bstack1l1lll1_opy_ (u"ࠦࡺࡴࡩࡵࡶࡨࡷࡹࠨሳ"), bstack1l1lll1_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧሴ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1l1lll1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧስ")) else fixturedef.get(bstack1l1lll1_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨሶ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1lll1_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨሷ")) else None
        node = request.node if hasattr(request, bstack1l1lll1_opy_ (u"ࠤࡱࡳࡩ࡫ࠢሸ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1lll1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥሹ")) else None
        baseid = fixturedef.get(bstack1l1lll1_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦሺ"), None) or bstack1l1lll1_opy_ (u"ࠧࠨሻ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1lll1_opy_ (u"ࠨ࡟ࡱࡻࡩࡹࡳࡩࡩࡵࡧࡰࠦሼ")):
            target = PytestBDDFramework.__1l1llll1ll1_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1lll1_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤሽ")) else None
            if target and not TestFramework.bstack1ll111lllll_opy_(target):
                self.__1ll1l11l1l1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡲࡴࡪࡥ࠾ࡽࡱࡳࡩ࡫ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥሾ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠤࠥሿ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣቀ") + str(target) + bstack1l1lll1_opy_ (u"ࠦࠧቁ"))
            return None
        instance = TestFramework.bstack1ll111lllll_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡧࡧࡳࡦ࡫ࡧࡁࢀࡨࡡࡴࡧ࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢቂ") + str(target) + bstack1l1lll1_opy_ (u"ࠨࠢቃ"))
            return None
        bstack1ll11l1ll1l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11llllll_opy_, {})
        if os.getenv(bstack1l1lll1_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡆࡊ࡚ࡗ࡙ࡗࡋࡓࠣቄ"), bstack1l1lll1_opy_ (u"ࠣ࠳ࠥቅ")) == bstack1l1lll1_opy_ (u"ࠤ࠴ࠦቆ"):
            bstack1ll111lll11_opy_ = bstack1l1lll1_opy_ (u"ࠥ࠾ࠧቇ").join((scope, fixturename))
            bstack1ll1l1l11ll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1111l111_opy_ = {
                bstack1l1lll1_opy_ (u"ࠦࡰ࡫ࡹࠣቈ"): bstack1ll111lll11_opy_,
                bstack1l1lll1_opy_ (u"ࠧࡺࡡࡨࡵࠥ቉"): PytestBDDFramework.__1ll1l111l1l_opy_(request.node, scenario),
                bstack1l1lll1_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࠢቊ"): fixturedef,
                bstack1l1lll1_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨቋ"): scope,
                bstack1l1lll1_opy_ (u"ࠣࡶࡼࡴࡪࠨቌ"): None,
            }
            try:
                if test_hook_state == bstack1lll1lll11l_opy_.POST and callable(getattr(args[-1], bstack1l1lll1_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨቍ"), None)):
                    bstack1ll1111l111_opy_[bstack1l1lll1_opy_ (u"ࠥࡸࡾࡶࡥࠣ቎")] = TestFramework.bstack1ll11l11lll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1111l111_opy_[bstack1l1lll1_opy_ (u"ࠦࡺࡻࡩࡥࠤ቏")] = uuid4().__str__()
                bstack1ll1111l111_opy_[PytestBDDFramework.bstack1ll11lll11l_opy_] = bstack1ll1l1l11ll_opy_
            elif test_hook_state == bstack1lll1lll11l_opy_.POST:
                bstack1ll1111l111_opy_[PytestBDDFramework.bstack1ll11l1ll11_opy_] = bstack1ll1l1l11ll_opy_
            if bstack1ll111lll11_opy_ in bstack1ll11l1ll1l_opy_:
                bstack1ll11l1ll1l_opy_[bstack1ll111lll11_opy_].update(bstack1ll1111l111_opy_)
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࠨቐ") + str(bstack1ll11l1ll1l_opy_[bstack1ll111lll11_opy_]) + bstack1l1lll1_opy_ (u"ࠨࠢቑ"))
            else:
                bstack1ll11l1ll1l_opy_[bstack1ll111lll11_opy_] = bstack1ll1111l111_opy_
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࢁࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࢂࠦࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࠥቒ") + str(len(bstack1ll11l1ll1l_opy_)) + bstack1l1lll1_opy_ (u"ࠣࠤቓ"))
        TestFramework.bstack1llll1lllll_opy_(instance, PytestBDDFramework.bstack1ll11llllll_opy_, bstack1ll11l1ll1l_opy_)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࡿࡱ࡫࡮ࠩࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶ࠭ࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤቔ") + str(instance.ref()) + bstack1l1lll1_opy_ (u"ࠥࠦቕ"))
        return instance
    def __1ll1l11l1l1_opy_(
        self,
        context: bstack1l1llllll1l_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll1lll1_opy_.create_context(target)
        ob = bstack1lll1llll11_opy_(ctx, self.bstack1ll1111l1l1_opy_, self.bstack1ll1ll11111_opy_, test_framework_state)
        TestFramework.bstack1ll1l111l11_opy_(ob, {
            TestFramework.bstack1llll1l111l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l1l111_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l1l111l_opy_: [],
            PytestBDDFramework.bstack1ll11llllll_opy_: {},
            PytestBDDFramework.bstack1ll11ll1111_opy_: {},
            PytestBDDFramework.bstack1ll11lll1ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1lllll_opy_(ob, TestFramework.bstack1ll11l1l1ll_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1lllll_opy_(ob, TestFramework.bstack1llll1l1ll1_opy_, context.platform_index)
        TestFramework.bstack1lll1l1l1l1_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡩࡴࡹ࠰࡬ࡨࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦቖ") + str(TestFramework.bstack1lll1l1l1l1_opy_.keys()) + bstack1l1lll1_opy_ (u"ࠧࠨ቗"))
        return ob
    @staticmethod
    def __1ll1111l11l_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1lll1_opy_ (u"࠭ࡩࡥࠩቘ"): id(step),
                bstack1l1lll1_opy_ (u"ࠧࡵࡧࡻࡸࠬ቙"): step.name,
                bstack1l1lll1_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩቚ"): step.keyword,
            })
        meta = {
            bstack1l1lll1_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪቛ"): {
                bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨቜ"): feature.name,
                bstack1l1lll1_opy_ (u"ࠫࡵࡧࡴࡩࠩቝ"): feature.filename,
                bstack1l1lll1_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ቞"): feature.description
            },
            bstack1l1lll1_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ቟"): {
                bstack1l1lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬበ"): scenario.name
            },
            bstack1l1lll1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧቡ"): steps,
            bstack1l1lll1_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫቢ"): PytestBDDFramework.__1ll1l11ll1l_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll111111l1_opy_: meta
            }
        )
    def bstack1ll11llll1l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1l1lll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡴࡲࡧࡪࡹࡳࡦࡵࠣࡸ࡭࡫ࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡵ࡬ࡱ࡮ࡲࡡࡳࠢࡷࡳࠥࡺࡨࡦࠢࡍࡥࡻࡧࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡯ࡳࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡄࡪࡨࡧࡰࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࡭ࡳࡹࡩࡥࡧࠣࢂ࠴࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠴࡛ࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡊࡴࡸࠠࡦࡣࡦ࡬ࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠮ࠣࡶࡪࡶ࡬ࡢࡥࡨࡷࠥࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧࠦࡩ࡯ࠢ࡬ࡸࡸࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡍ࡫ࠦࡡࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡰࡥࡹࡩࡨࡦࡵࠣࡥࠥࡳ࡯ࡥ࡫ࡩ࡭ࡪࡪࠠࡩࡱࡲ࡯࠲ࡲࡥࡷࡧ࡯ࠤ࡫࡯࡬ࡦ࠮ࠣ࡭ࡹࠦࡣࡳࡧࡤࡸࡪࡹࠠࡢࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࠤࡼ࡯ࡴࡩࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡤࡦࡶࡤ࡭ࡱࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡓࡪ࡯࡬ࡰࡦࡸ࡬ࡺ࠮ࠣ࡭ࡹࠦࡰࡳࡱࡦࡩࡸࡹࡥࡴࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡱࡵࡣࡢࡶࡨࡨࠥ࡯࡮ࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡦࡾࠦࡲࡦࡲ࡯ࡥࡨ࡯࡮ࡨࠢࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢࠡࡹ࡬ࡸ࡭ࠦࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡗ࡬ࡪࠦࡣࡳࡧࡤࡸࡪࡪࠠࡍࡱࡪࡉࡳࡺࡲࡺࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡥࡷ࡫ࠠࡢࡦࡧࡩࡩࠦࡴࡰࠢࡷ࡬ࡪࠦࡨࡰࡱ࡮ࠫࡸࠦࠢ࡭ࡱࡪࡷࠧࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡬ࡴࡵ࡫࠻ࠢࡗ࡬ࡪࠦࡥࡷࡧࡱࡸࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࠦࡡ࡯ࡦࠣ࡬ࡴࡵ࡫ࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤ࡙࡫ࡳࡵࡎࡨࡺࡪࡲࠠ࡮ࡱࡱ࡭ࡹࡵࡲࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡺ࡯࡬ࡥࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠ࡮ࡱࡱ࡭ࡹࡵࡲࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤባ")
        global _1ll11l11ll1_opy_
        platform_index = os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫቤ")]
        bstack1ll11l111l1_opy_ = os.path.join(bstack1ll1l111ll1_opy_, (bstack1ll1l11ll11_opy_ + str(platform_index)), bstack1ll11ll1lll_opy_)
        if not os.path.exists(bstack1ll11l111l1_opy_) or not os.path.isdir(bstack1ll11l111l1_opy_):
            return
        logs = hook.get(bstack1l1lll1_opy_ (u"ࠧࡲ࡯ࡨࡵࠥብ"), [])
        with os.scandir(bstack1ll11l111l1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l11ll1_opy_:
                    self.logger.info(bstack1l1lll1_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦቦ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1l1lll1_opy_ (u"ࠢࠣቧ")
                    log_entry = bstack1ll11ll1ll1_opy_(
                        kind=bstack1l1lll1_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥቨ"),
                        message=bstack1l1lll1_opy_ (u"ࠤࠥቩ"),
                        level=bstack1l1lll1_opy_ (u"ࠥࠦቪ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1llllllll_opy_=entry.stat().st_size,
                        bstack1ll111l11ll_opy_=bstack1l1lll1_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦቫ"),
                        bstack11l1l_opy_=os.path.abspath(entry.path),
                        bstack1ll1l1llll1_opy_=hook.get(TestFramework.bstack1ll11l111ll_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l11ll1_opy_.add(abs_path)
        platform_index = os.environ[bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬቬ")]
        bstack1ll1l11lll1_opy_ = os.path.join(bstack1ll1l111ll1_opy_, (bstack1ll1l11ll11_opy_ + str(platform_index)), bstack1ll11ll1lll_opy_, bstack1ll1111lll1_opy_)
        if not os.path.exists(bstack1ll1l11lll1_opy_) or not os.path.isdir(bstack1ll1l11lll1_opy_):
            self.logger.info(bstack1l1lll1_opy_ (u"ࠨࡎࡰࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡩࡳࡺࡴࡤࠡࡣࡷ࠾ࠥࢁࡽࠣቭ").format(bstack1ll1l11lll1_opy_))
        else:
            self.logger.info(bstack1l1lll1_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡨࡵࡳࡲࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠼ࠣࡿࢂࠨቮ").format(bstack1ll1l11lll1_opy_))
            with os.scandir(bstack1ll1l11lll1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l11ll1_opy_:
                        self.logger.info(bstack1l1lll1_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨቯ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1l1lll1_opy_ (u"ࠤࠥተ")
                        log_entry = bstack1ll11ll1ll1_opy_(
                            kind=bstack1l1lll1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧቱ"),
                            message=bstack1l1lll1_opy_ (u"ࠦࠧቲ"),
                            level=bstack1l1lll1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤታ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1llllllll_opy_=entry.stat().st_size,
                            bstack1ll111l11ll_opy_=bstack1l1lll1_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨቴ"),
                            bstack11l1l_opy_=os.path.abspath(entry.path),
                            bstack1l1llll1l1l_opy_=hook.get(TestFramework.bstack1ll11l111ll_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l11ll1_opy_.add(abs_path)
        hook[bstack1l1lll1_opy_ (u"ࠢ࡭ࡱࡪࡷࠧት")] = logs
    def bstack1ll111l1l11_opy_(
        self,
        bstack1ll1l1111ll_opy_: bstack1lll1llll11_opy_,
        entries: List[bstack1ll11ll1ll1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡕࡈࡗࡘࡏࡏࡏࡡࡌࡈࠧቶ"))
        req.platform_index = TestFramework.get_state(bstack1ll1l1111ll_opy_, TestFramework.bstack1llll1l1ll1_opy_)
        req.execution_context.hash = str(bstack1ll1l1111ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1l1111ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1l1111ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1l1111ll_opy_, TestFramework.bstack1llll1l111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1l1111ll_opy_, TestFramework.bstack1lll1l1l111_opy_)
            log_entry.uuid = entry.bstack1ll1l1llll1_opy_ if entry.bstack1ll1l1llll1_opy_ else TestFramework.get_state(bstack1ll1l1111ll_opy_, TestFramework.bstack1llll11lll1_opy_)
            log_entry.test_framework_state = bstack1ll1l1111ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1lll1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣቷ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l1lll1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧቸ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1llllllll_opy_
                log_entry.file_path = entry.bstack11l1l_opy_
        def bstack1ll111lll1l_opy_():
            bstack11ll11ll1_opy_ = datetime.now()
            try:
                self.bstack1lllll1ll11_opy_.LogCreatedEvent(req)
                bstack1ll1l1111ll_opy_.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠣቹ"), datetime.now() - bstack11ll11ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1lll1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡽࢀࠦቺ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lll1l_opy_.enqueue(bstack1ll111lll1l_opy_)
    def __1ll1l111111_opy_(self, instance) -> None:
        bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡐࡴࡧࡤࡴࠢࡦࡹࡸࡺ࡯࡮ࠢࡷࡥ࡬ࡹࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡩ࡬ࡺࡪࡴࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡲࡦࡣࡷࡩࡸࠦࡡࠡࡦ࡬ࡧࡹࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡸࡪࡹࡴࠡ࡮ࡨࡺࡪࡲࠠࡤࡷࡶࡸࡴࡳࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡹࡸࡩࡦࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡻࡳࡵࡱࡰࡘࡦ࡭ࡍࡢࡰࡤ࡫ࡪࡸࠠࡢࡰࡧࠤࡺࡶࡤࡢࡶࡨࡷࠥࡺࡨࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡸࡺࡡࡵࡧࠣࡹࡸ࡯࡮ࡨࠢࡶࡩࡹࡥࡳࡵࡣࡷࡩࡤ࡫࡮ࡵࡴ࡬ࡩࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦቻ")
        bstack1ll1l11l1ll_opy_ = {bstack1l1lll1_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠤቼ"): bstack1ll1111ll1l_opy_.bstack1ll1l1l1ll1_opy_()}
        TestFramework.bstack1ll1l111l11_opy_(instance, bstack1ll1l11l1ll_opy_)
    @staticmethod
    def __1ll11l11l1l_opy_(instance, args):
        request, bstack1l1llll1l11_opy_ = args
        bstack1ll1l1lll1l_opy_ = id(bstack1l1llll1l11_opy_)
        bstack1ll11ll1l1l_opy_ = instance.data[TestFramework.bstack1ll111111l1_opy_]
        step = next(filter(lambda st: st[bstack1l1lll1_opy_ (u"ࠨ࡫ࡧࠫች")] == bstack1ll1l1lll1l_opy_, bstack1ll11ll1l1l_opy_[bstack1l1lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨቾ")]), None)
        step.update({
            bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧቿ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11ll1l1l_opy_[bstack1l1lll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኀ")]) if st[bstack1l1lll1_opy_ (u"ࠬ࡯ࡤࠨኁ")] == step[bstack1l1lll1_opy_ (u"࠭ࡩࡥࠩኂ")]), None)
        if index is not None:
            bstack1ll11ll1l1l_opy_[bstack1l1lll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኃ")][index] = step
        instance.data[TestFramework.bstack1ll111111l1_opy_] = bstack1ll11ll1l1l_opy_
    @staticmethod
    def __1ll111ll11l_opy_(instance, args):
        bstack1l1lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡽࡨࡦࡰࠣࡰࡪࡴࠠࡢࡴࡪࡷࠥ࡯ࡳࠡ࠴࠯ࠤ࡮ࡺࠠࡴ࡫ࡪࡲ࡮࡬ࡩࡦࡵࠣࡸ࡭࡫ࡲࡦࠢ࡬ࡷࠥࡴ࡯ࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡶ࡬ࡹࠠࡢࡴࡨࠤ࠲࡛ࠦࡳࡧࡴࡹࡪࡹࡴ࠭ࠢࡶࡸࡪࡶ࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥࡧࡲࡨࡵࠣࡥࡷ࡫ࠠ࠴ࠢࡷ࡬ࡪࡴࠠࡵࡪࡨࠤࡱࡧࡳࡵࠢࡹࡥࡱࡻࡥࠡ࡫ࡶࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦኄ")
        bstack1l1lllll1ll_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1l1llll1l11_opy_ = args[1]
        bstack1ll1l1lll1l_opy_ = id(bstack1l1llll1l11_opy_)
        bstack1ll11ll1l1l_opy_ = instance.data[TestFramework.bstack1ll111111l1_opy_]
        step = None
        if bstack1ll1l1lll1l_opy_ is not None and bstack1ll11ll1l1l_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኅ")):
            step = next(filter(lambda st: st[bstack1l1lll1_opy_ (u"ࠪ࡭ࡩ࠭ኆ")] == bstack1ll1l1lll1l_opy_, bstack1ll11ll1l1l_opy_[bstack1l1lll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኇ")]), None)
            step.update({
                bstack1l1lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪኈ"): bstack1l1lllll1ll_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1l1lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭኉"): bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧኊ"),
                bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩኋ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1l1lll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩኌ"): bstack1l1lll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪኍ"),
                })
        index = next((i for i, st in enumerate(bstack1ll11ll1l1l_opy_[bstack1l1lll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ኎")]) if st[bstack1l1lll1_opy_ (u"ࠬ࡯ࡤࠨ኏")] == step[bstack1l1lll1_opy_ (u"࠭ࡩࡥࠩነ")]), None)
        if index is not None:
            bstack1ll11ll1l1l_opy_[bstack1l1lll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኑ")][index] = step
        instance.data[TestFramework.bstack1ll111111l1_opy_] = bstack1ll11ll1l1l_opy_
    @staticmethod
    def __1ll1l11ll1l_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1l1lll1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪኒ")):
                examples = list(node.callspec.params[bstack1l1lll1_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨና")].values())
            return examples
        except:
            return []
    def bstack1ll11lll1l1_opy_(self, instance: bstack1lll1llll11_opy_, bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_]):
        bstack1ll111l1ll1_opy_ = (
            PytestBDDFramework.bstack1ll111l1lll_opy_
            if bstack1lllll1llll_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else PytestBDDFramework.bstack1ll1111l1ll_opy_
        )
        hook = PytestBDDFramework.bstack1ll1l1l11l1_opy_(instance, bstack1ll111l1ll1_opy_)
        entries = hook.get(TestFramework.bstack1ll1111111l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l1l111l_opy_, []))
        return entries
    def bstack1ll11ll111l_opy_(self, instance: bstack1lll1llll11_opy_, bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_]):
        bstack1ll111l1ll1_opy_ = (
            PytestBDDFramework.bstack1ll111l1lll_opy_
            if bstack1lllll1llll_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else PytestBDDFramework.bstack1ll1111l1ll_opy_
        )
        PytestBDDFramework.bstack1ll11l1111l_opy_(instance, bstack1ll111l1ll1_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l1l111l_opy_, []).clear()
    @staticmethod
    def bstack1ll1l1l11l1_opy_(instance: bstack1lll1llll11_opy_, bstack1ll111l1ll1_opy_: str):
        bstack1ll1111ll11_opy_ = (
            PytestBDDFramework.bstack1ll11ll1111_opy_
            if bstack1ll111l1ll1_opy_ == PytestBDDFramework.bstack1ll1111l1ll_opy_
            else PytestBDDFramework.bstack1ll11lll1ll_opy_
        )
        bstack1ll1l1l1111_opy_ = TestFramework.get_state(instance, bstack1ll111l1ll1_opy_, None)
        bstack1ll11l1lll1_opy_ = TestFramework.get_state(instance, bstack1ll1111ll11_opy_, None) if bstack1ll1l1l1111_opy_ else None
        return (
            bstack1ll11l1lll1_opy_[bstack1ll1l1l1111_opy_][-1]
            if isinstance(bstack1ll11l1lll1_opy_, dict) and len(bstack1ll11l1lll1_opy_.get(bstack1ll1l1l1111_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11l1111l_opy_(instance: bstack1lll1llll11_opy_, bstack1ll111l1ll1_opy_: str):
        hook = PytestBDDFramework.bstack1ll1l1l11l1_opy_(instance, bstack1ll111l1ll1_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1111111l_opy_, []).clear()
    @staticmethod
    def __1l1lllll1l1_opy_(instance: bstack1lll1llll11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1lll1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡦࡳࡷࡪࡳࠣኔ"), None)):
            return
        if os.getenv(bstack1l1lll1_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡐࡔࡍࡓࠣን"), bstack1l1lll1_opy_ (u"ࠧ࠷ࠢኖ")) != bstack1l1lll1_opy_ (u"ࠨ࠱ࠣኗ"):
            PytestBDDFramework.logger.warning(bstack1l1lll1_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡯࡮ࡨࠢࡦࡥࡵࡲ࡯ࡨࠤኘ"))
            return
        bstack1ll11ll11ll_opy_ = {
            bstack1l1lll1_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢኙ"): (PytestBDDFramework.bstack1ll111l1lll_opy_, PytestBDDFramework.bstack1ll11lll1ll_opy_),
            bstack1l1lll1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦኚ"): (PytestBDDFramework.bstack1ll1111l1ll_opy_, PytestBDDFramework.bstack1ll11ll1111_opy_),
        }
        for when in (bstack1l1lll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤኛ"), bstack1l1lll1_opy_ (u"ࠦࡨࡧ࡬࡭ࠤኜ"), bstack1l1lll1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢኝ")):
            bstack1ll111ll111_opy_ = args[1].get_records(when)
            if not bstack1ll111ll111_opy_:
                continue
            records = [
                bstack1ll11ll1ll1_opy_(
                    kind=TestFramework.bstack1ll1l1ll1l1_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1lll1_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠤኞ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1lll1_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࠣኟ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll111ll111_opy_
                if isinstance(getattr(r, bstack1l1lll1_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤአ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll111ll1ll_opy_, bstack1ll1111ll11_opy_ = bstack1ll11ll11ll_opy_.get(when, (None, None))
            bstack1ll1ll111l1_opy_ = TestFramework.get_state(instance, bstack1ll111ll1ll_opy_, None) if bstack1ll111ll1ll_opy_ else None
            bstack1ll11l1lll1_opy_ = TestFramework.get_state(instance, bstack1ll1111ll11_opy_, None) if bstack1ll1ll111l1_opy_ else None
            if isinstance(bstack1ll11l1lll1_opy_, dict) and len(bstack1ll11l1lll1_opy_.get(bstack1ll1ll111l1_opy_, [])) > 0:
                hook = bstack1ll11l1lll1_opy_[bstack1ll1ll111l1_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1111111l_opy_ in hook:
                    hook[TestFramework.bstack1ll1111111l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l1l111l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l111lll_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll11111ll1_opy_(request.node, scenario)
        bstack1ll111llll1_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll111llll1_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1llll11lll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l1l1l1l_opy_: test_id,
            TestFramework.bstack1ll11ll11l1_opy_: test_name,
            TestFramework.bstack1ll111ll1l1_opy_: test_id,
            TestFramework.bstack1ll111l1111_opy_: bstack1ll111llll1_opy_,
            TestFramework.bstack1ll11111l1l_opy_: PytestBDDFramework.__1ll1l111l1l_opy_(feature, scenario),
            TestFramework.bstack1ll11l1llll_opy_: code,
            TestFramework.bstack1lll1l11111_opy_: TestFramework.bstack1ll11l1l11l_opy_,
            TestFramework.bstack1lll111lll1_opy_: test_name
        }
    @staticmethod
    def __1ll11111ll1_opy_(node, scenario):
        if hasattr(node, bstack1l1lll1_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫኡ")):
            parts = node.nodeid.rsplit(bstack1l1lll1_opy_ (u"ࠥ࡟ࠧኢ"))
            params = parts[-1]
            return bstack1l1lll1_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦኣ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll1l111l1l_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1l1lll1_opy_ (u"ࠬࡺࡡࡨࡵࠪኤ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1l1lll1_opy_ (u"࠭ࡴࡢࡩࡶࠫእ")) else [])
    @staticmethod
    def __1l1llll1ll1_opy_(location):
        return bstack1l1lll1_opy_ (u"ࠢ࠻࠼ࠥኦ").join(filter(lambda x: isinstance(x, str), location))