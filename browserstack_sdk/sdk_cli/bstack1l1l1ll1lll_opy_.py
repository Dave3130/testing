# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1ll11111_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11ll1ll_opy_ import bstack1ll11l1l1ll_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll11l1_opy_,
    bstack1lll1l1l11l_opy_,
    bstack1lll1l1llll_opy_,
    bstack1l1llll111l_opy_,
    bstack1ll1l1l1l11_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll111lll11_opy_
from bstack_utils.bstack1l111l1l1_opy_ import bstack1lllllll1ll_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l1111_opy_
from browserstack_sdk.sdk_cli.utils.bstack1l1lllll11l_opy_ import bstack1ll11l1llll_opy_
from bstack_utils.bstack1l11ll11_opy_ import bstack1l1l111l_opy_
bstack1ll11l1l1l1_opy_ = bstack1ll111lll11_opy_()
bstack1ll1l1l11ll_opy_ = 1.0
bstack1ll11111lll_opy_ = bstack11l11ll_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᖙ")
bstack11lll1lll11_opy_ = bstack11l11ll_opy_ (u"ࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥᖚ")
bstack11lll1lll1l_opy_ = bstack11l11ll_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᖛ")
bstack11llll11111_opy_ = bstack11l11ll_opy_ (u"ࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧᖜ")
bstack11lll1llll1_opy_ = bstack11l11ll_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤᖝ")
_1ll1l11l1ll_opy_ = set()
class bstack1l11lll1111_opy_(TestFramework):
    bstack1ll111l1l11_opy_ = bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᖞ")
    bstack1ll1111l111_opy_ = bstack11l11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࠥᖟ")
    bstack1ll11lll11l_opy_ = bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧᖠ")
    bstack1ll1l1111l1_opy_ = bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡰࡦࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࠤᖡ")
    bstack1ll11l11l1l_opy_ = bstack11l11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦᖢ")
    bstack1ll11l11111_opy_: bool
    bstack1lll11l11l1_opy_: bstack1lll11l1111_opy_  = None
    bstack1llll1l1ll1_opy_ = None
    bstack1ll111ll1l1_opy_ = [
        bstack1lll1ll11l1_opy_.BEFORE_ALL,
        bstack1lll1ll11l1_opy_.AFTER_ALL,
        bstack1lll1ll11l1_opy_.BEFORE_EACH,
        bstack1lll1ll11l1_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11l1l111_opy_: Dict[str, str],
        bstack1ll11ll1l1l_opy_: List[str]=[bstack11l11ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤᖣ")],
        bstack1lll11l11l1_opy_: bstack1lll11l1111_opy_=None,
        bstack1llll1l1ll1_opy_=None
    ):
        super().__init__(bstack1ll11ll1l1l_opy_, bstack1ll11l1l111_opy_, bstack1lll11l11l1_opy_)
        self.bstack1ll11l11111_opy_ = any(bstack11l11ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᖤ") in item.lower() for item in bstack1ll11ll1l1l_opy_)
        self.bstack1llll1l1ll1_opy_ = bstack1llll1l1ll1_opy_
    def track_event(
        self,
        context: bstack1l1llll111l_opy_,
        test_framework_state: bstack1lll1ll11l1_opy_,
        test_hook_state: bstack1lll1l1llll_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll11l1_opy_.TEST or test_framework_state in bstack1l11lll1111_opy_.bstack1ll111ll1l1_opy_:
            bstack1ll11l1l1ll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll11l1_opy_.NONE:
            self.logger.warning(bstack11l11ll_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨࡨࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࠧᖥ") + str(test_hook_state) + bstack11l11ll_opy_ (u"ࠧࠨᖦ"))
            return
        if not self.bstack1ll11l11111_opy_:
            self.logger.warning(bstack11l11ll_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡃࠢᖧ") + str(str(self.bstack1ll11ll1l1l_opy_)) + bstack11l11ll_opy_ (u"ࠢࠣᖨ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l11ll_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᖩ") + str(kwargs) + bstack11l11ll_opy_ (u"ࠤࠥᖪ"))
            return
        instance = self.__1ll1l11llll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡥࡷ࡭ࡳ࠾ࠤᖫ") + str(args) + bstack11l11ll_opy_ (u"ࠦࠧᖬ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l11lll1111_opy_.bstack1ll111ll1l1_opy_ and test_hook_state == bstack1lll1l1llll_opy_.PRE:
                bstack1ll11l11lll_opy_ = bstack1lllllll1ll_opy_.bstack1ll11l111ll_opy_(EVENTS.bstack1ll11l11l1_opy_.value)
                name = str(EVENTS.bstack1ll11l11l1_opy_.name)+bstack11l11ll_opy_ (u"ࠧࡀࠢᖭ")+str(test_framework_state.name)
                TestFramework.bstack1ll111l11ll_opy_(instance, name, bstack1ll11l11lll_opy_)
        except Exception as e:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳࠢࡳࡶࡪࡀࠠࡼࡿࠥᖮ").format(e))
        try:
            if not TestFramework.bstack1llllll11l1_opy_(instance, TestFramework.bstack1ll1l111l1l_opy_) and test_hook_state == bstack1lll1l1llll_opy_.PRE:
                test = bstack1l11lll1111_opy_.__1l1llll1ll1_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack11l11ll_opy_ (u"ࠢ࡭ࡱࡤࡨࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢᖯ") + str(test_hook_state) + bstack11l11ll_opy_ (u"ࠣࠤᖰ"))
            if test_framework_state == bstack1lll1ll11l1_opy_.TEST:
                if test_hook_state == bstack1lll1l1llll_opy_.PRE and not TestFramework.bstack1llllll11l1_opy_(instance, TestFramework.bstack1ll11lll1l1_opy_):
                    TestFramework.bstack1llll1l1l11_opy_(instance, TestFramework.bstack1ll11lll1l1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l11ll_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡸࡺࡡࡳࡶࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢᖱ") + str(test_hook_state) + bstack11l11ll_opy_ (u"ࠥࠦᖲ"))
                elif test_hook_state == bstack1lll1l1llll_opy_.POST and not TestFramework.bstack1llllll11l1_opy_(instance, TestFramework.bstack1ll11ll11l1_opy_):
                    TestFramework.bstack1llll1l1l11_opy_(instance, TestFramework.bstack1ll11ll11l1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡥ࡯ࡦࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢᖳ") + str(test_hook_state) + bstack11l11ll_opy_ (u"ࠧࠨᖴ"))
            elif test_framework_state == bstack1lll1ll11l1_opy_.LOG and test_hook_state == bstack1lll1l1llll_opy_.POST:
                bstack1l11lll1111_opy_.__1ll1111ll1l_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll11l1_opy_.LOG_REPORT and test_hook_state == bstack1lll1l1llll_opy_.POST:
                self.__1ll111l1l1l_opy_(instance, *args)
                self.__1ll111ll11l_opy_(instance)
            elif test_framework_state in bstack1l11lll1111_opy_.bstack1ll111ll1l1_opy_:
                self.__1ll1l11lll1_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᖵ") + str(instance.ref()) + bstack11l11ll_opy_ (u"ࠢࠣᖶ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1l1l1111_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l11lll1111_opy_.bstack1ll111ll1l1_opy_ and test_hook_state == bstack1lll1l1llll_opy_.POST:
                name = str(EVENTS.bstack1ll11l11l1_opy_.name)+bstack11l11ll_opy_ (u"ࠣ࠼ࠥᖷ")+str(test_framework_state.name)
                bstack1ll11l11lll_opy_ = TestFramework.bstack1ll111l1lll_opy_(instance, name)
                bstack1lllllll1ll_opy_.end(EVENTS.bstack1ll11l11l1_opy_.value, bstack1ll11l11lll_opy_+bstack11l11ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᖸ"), bstack1ll11l11lll_opy_+bstack11l11ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᖹ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᖺ").format(e))
    def bstack1ll111lll1l_opy_(self):
        return self.bstack1ll11l11111_opy_
    def __1l1llll1l1l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l11ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡸࡻ࡬ࡵࠤᖻ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11111111_opy_(rep, [bstack11l11ll_opy_ (u"ࠨࡷࡩࡧࡱࠦᖼ"), bstack11l11ll_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᖽ"), bstack11l11ll_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣᖾ"), bstack11l11ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᖿ"), bstack11l11ll_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠦᗀ"), bstack11l11ll_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥᗁ")])
        return None
    def __1ll111l1l1l_opy_(self, instance: bstack1lll1l1l11l_opy_, *args):
        result = self.__1l1llll1l1l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111111ll_opy_ = None
        if result.get(bstack11l11ll_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᗂ"), None) == bstack11l11ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᗃ") and len(args) > 1 and getattr(args[1], bstack11l11ll_opy_ (u"ࠢࡦࡺࡦ࡭ࡳ࡬࡯ࠣᗄ"), None) is not None:
            failure = [{bstack11l11ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᗅ"): [args[1].excinfo.exconly(), result.get(bstack11l11ll_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣᗆ"), None)]}]
            bstack11111111ll_opy_ = bstack11l11ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᗇ") if bstack11l11ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᗈ") in getattr(args[1].excinfo, bstack11l11ll_opy_ (u"ࠧࡺࡹࡱࡧࡱࡥࡲ࡫ࠢᗉ"), bstack11l11ll_opy_ (u"ࠨࠢᗊ")) else bstack11l11ll_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᗋ")
        bstack1ll111l111l_opy_ = result.get(bstack11l11ll_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᗌ"), TestFramework.bstack1ll1111l1l1_opy_)
        if bstack1ll111l111l_opy_ != TestFramework.bstack1ll1111l1l1_opy_:
            TestFramework.bstack1llll1l1l11_opy_(instance, TestFramework.bstack1l1lllll1ll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11ll1111_opy_(instance, {
            TestFramework.bstack1lll1l1l1l1_opy_: failure,
            TestFramework.bstack1l1lll1l1ll_opy_: bstack11111111ll_opy_,
            TestFramework.bstack1lll11l1l11_opy_: bstack1ll111l111l_opy_,
        })
    def __1ll1l11llll_opy_(
        self,
        context: bstack1l1llll111l_opy_,
        test_framework_state: bstack1lll1ll11l1_opy_,
        test_hook_state: bstack1lll1l1llll_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll11l1_opy_.SETUP_FIXTURE:
            instance = self.__1ll111ll1ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1111l1ll_opy_ bstack1ll1l11l11l_opy_ this to be bstack11l11ll_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᗍ")
            if test_framework_state == bstack1lll1ll11l1_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll111111l1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll11l1_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l11ll_opy_ (u"ࠥࡲࡴࡪࡥࠣᗎ"), None), bstack11l11ll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᗏ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l11ll_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᗐ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11l11ll1_opy_(target) if target else None
        return instance
    def __1ll1l11lll1_opy_(
        self,
        instance: bstack1lll1l1l11l_opy_,
        test_framework_state: bstack1lll1ll11l1_opy_,
        test_hook_state: bstack1lll1l1llll_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l111l11_opy_ = TestFramework.get_state(instance, bstack1l11lll1111_opy_.bstack1ll1111l111_opy_, {})
        if not key in bstack1ll1l111l11_opy_:
            bstack1ll1l111l11_opy_[key] = []
        bstack1ll111111ll_opy_ = TestFramework.get_state(instance, bstack1l11lll1111_opy_.bstack1ll11lll11l_opy_, {})
        if not key in bstack1ll111111ll_opy_:
            bstack1ll111111ll_opy_[key] = []
        bstack1ll1111111l_opy_ = {
            bstack1l11lll1111_opy_.bstack1ll1111l111_opy_: bstack1ll1l111l11_opy_,
            bstack1l11lll1111_opy_.bstack1ll11lll11l_opy_: bstack1ll111111ll_opy_,
        }
        if test_hook_state == bstack1lll1l1llll_opy_.PRE:
            hook = {
                bstack11l11ll_opy_ (u"ࠨ࡫ࡦࡻࠥᗑ"): key,
                TestFramework.bstack1ll11llll11_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l1lll1_opy_: TestFramework.bstack1l1lllll1l1_opy_,
                TestFramework.bstack1ll1l11ll1l_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1l1llll1l11_opy_: [],
                TestFramework.bstack1l1lll1l111_opy_: args[1] if len(args) > 1 else bstack11l11ll_opy_ (u"ࠧࠨᗒ"),
                TestFramework.bstack1ll1l1l1l1l_opy_: bstack1ll11l1llll_opy_.bstack1l1lllll111_opy_()
            }
            bstack1ll1l111l11_opy_[key].append(hook)
            bstack1ll1111111l_opy_[bstack1l11lll1111_opy_.bstack1ll1l1111l1_opy_] = key
        elif test_hook_state == bstack1lll1l1llll_opy_.POST:
            bstack1ll111l11l1_opy_ = bstack1ll1l111l11_opy_.get(key, [])
            hook = bstack1ll111l11l1_opy_.pop() if bstack1ll111l11l1_opy_ else None
            if hook:
                result = self.__1l1llll1l1l_opy_(*args)
                if result:
                    bstack1ll1l111ll1_opy_ = result.get(bstack11l11ll_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᗓ"), TestFramework.bstack1l1lllll1l1_opy_)
                    if bstack1ll1l111ll1_opy_ != TestFramework.bstack1l1lllll1l1_opy_:
                        hook[TestFramework.bstack1ll11l1lll1_opy_] = bstack1ll1l111ll1_opy_
                hook[TestFramework.bstack1l1lll1ll11_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l1l1l1l_opy_]= bstack1ll11l1llll_opy_.bstack1l1lllll111_opy_()
                self.bstack1ll11ll111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l1l111l_opy_, [])
                if logs: self.bstack1ll11l1ll11_opy_(instance, logs)
                bstack1ll111111ll_opy_[key].append(hook)
                bstack1ll1111111l_opy_[bstack1l11lll1111_opy_.bstack1ll11l11l1l_opy_] = key
        TestFramework.bstack1ll11ll1111_opy_(instance, bstack1ll1111111l_opy_)
        self.logger.debug(bstack11l11ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡪࡲࡳࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽ࡮ࡩࡾࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࡁࢀ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࢂࠦࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࠽ࠣᗔ") + str(bstack1ll111111ll_opy_) + bstack11l11ll_opy_ (u"ࠥࠦᗕ"))
    def __1ll111ll1ll_opy_(
        self,
        context: bstack1l1llll111l_opy_,
        test_framework_state: bstack1lll1ll11l1_opy_,
        test_hook_state: bstack1lll1l1llll_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11111111_opy_(args[0], [bstack11l11ll_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᗖ"), bstack11l11ll_opy_ (u"ࠧࡧࡲࡨࡰࡤࡱࡪࠨᗗ"), bstack11l11ll_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨᗘ"), bstack11l11ll_opy_ (u"ࠢࡪࡦࡶࠦᗙ"), bstack11l11ll_opy_ (u"ࠣࡷࡱ࡭ࡹࡺࡥࡴࡶࠥᗚ"), bstack11l11ll_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤᗛ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack11l11ll_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᗜ")) else fixturedef.get(bstack11l11ll_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᗝ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l11ll_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࠥᗞ")) else None
        node = request.node if hasattr(request, bstack11l11ll_opy_ (u"ࠨ࡮ࡰࡦࡨࠦᗟ")) else None
        target = request.node.nodeid if hasattr(node, bstack11l11ll_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᗠ")) else None
        baseid = fixturedef.get(bstack11l11ll_opy_ (u"ࠣࡤࡤࡷࡪ࡯ࡤࠣᗡ"), None) or bstack11l11ll_opy_ (u"ࠤࠥᗢ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l11ll_opy_ (u"ࠥࡣࡵࡿࡦࡶࡰࡦ࡭ࡹ࡫࡭ࠣᗣ")):
            target = bstack1l11lll1111_opy_.__1l1llll11ll_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l11ll_opy_ (u"ࠦࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᗤ")) else None
            if target and not TestFramework.bstack1ll11l11ll1_opy_(target):
                self.__1ll111111l1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠ࡯ࡱࡧࡩࡂࢁ࡮ࡰࡦࡨࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢᗥ") + str(test_hook_state) + bstack11l11ll_opy_ (u"ࠨࠢᗦ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l11ll_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࡂࢁࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧᗧ") + str(target) + bstack11l11ll_opy_ (u"ࠣࠤᗨ"))
            return None
        instance = TestFramework.bstack1ll11l11ll1_opy_(target)
        if not instance:
            self.logger.warning(bstack11l11ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡤࡤࡷࡪ࡯ࡤ࠾ࡽࡥࡥࡸ࡫ࡩࡥࡿࠣࡸࡦࡸࡧࡦࡶࡀࠦᗩ") + str(target) + bstack11l11ll_opy_ (u"ࠥࠦᗪ"))
            return None
        bstack1ll11ll1ll1_opy_ = TestFramework.get_state(instance, bstack1l11lll1111_opy_.bstack1ll111l1l11_opy_, {})
        if os.getenv(bstack11l11ll_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡊࡎ࡞ࡔࡖࡔࡈࡗࠧᗫ"), bstack11l11ll_opy_ (u"ࠧ࠷ࠢᗬ")) == bstack11l11ll_opy_ (u"ࠨ࠱ࠣᗭ"):
            bstack1ll11111ll1_opy_ = bstack11l11ll_opy_ (u"ࠢ࠻ࠤᗮ").join((scope, fixturename))
            bstack1ll11l1111l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11ll1lll_opy_ = {
                bstack11l11ll_opy_ (u"ࠣ࡭ࡨࡽࠧᗯ"): bstack1ll11111ll1_opy_,
                bstack11l11ll_opy_ (u"ࠤࡷࡥ࡬ࡹࠢᗰ"): bstack1l11lll1111_opy_.__1ll111ll111_opy_(request.node),
                bstack11l11ll_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࠦᗱ"): fixturedef,
                bstack11l11ll_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᗲ"): scope,
                bstack11l11ll_opy_ (u"ࠧࡺࡹࡱࡧࠥᗳ"): None,
            }
            try:
                if test_hook_state == bstack1lll1l1llll_opy_.POST and callable(getattr(args[-1], bstack11l11ll_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥᗴ"), None)):
                    bstack1ll11ll1lll_opy_[bstack11l11ll_opy_ (u"ࠢࡵࡻࡳࡩࠧᗵ")] = TestFramework.bstack1ll11l11l11_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1l1llll_opy_.PRE:
                bstack1ll11ll1lll_opy_[bstack11l11ll_opy_ (u"ࠣࡷࡸ࡭ࡩࠨᗶ")] = uuid4().__str__()
                bstack1ll11ll1lll_opy_[bstack1l11lll1111_opy_.bstack1ll1l11ll1l_opy_] = bstack1ll11l1111l_opy_
            elif test_hook_state == bstack1lll1l1llll_opy_.POST:
                bstack1ll11ll1lll_opy_[bstack1l11lll1111_opy_.bstack1l1lll1ll11_opy_] = bstack1ll11l1111l_opy_
            if bstack1ll11111ll1_opy_ in bstack1ll11ll1ll1_opy_:
                bstack1ll11ll1ll1_opy_[bstack1ll11111ll1_opy_].update(bstack1ll11ll1lll_opy_)
                self.logger.debug(bstack11l11ll_opy_ (u"ࠤࡸࡴࡩࡧࡴࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦ࠿ࠥᗷ") + str(bstack1ll11ll1ll1_opy_[bstack1ll11111ll1_opy_]) + bstack11l11ll_opy_ (u"ࠥࠦᗸ"))
            else:
                bstack1ll11ll1ll1_opy_[bstack1ll11111ll1_opy_] = bstack1ll11ll1lll_opy_
                self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦ࠿ࡾࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡿࠣࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࡃࠢᗹ") + str(len(bstack1ll11ll1ll1_opy_)) + bstack11l11ll_opy_ (u"ࠧࠨᗺ"))
        TestFramework.bstack1llll1l1l11_opy_(instance, bstack1l11lll1111_opy_.bstack1ll111l1l11_opy_, bstack1ll11ll1ll1_opy_)
        self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࡼ࡮ࡨࡲ࠭ࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠪࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᗻ") + str(instance.ref()) + bstack11l11ll_opy_ (u"ࠢࠣᗼ"))
        return instance
    def __1ll111111l1_opy_(
        self,
        context: bstack1l1llll111l_opy_,
        test_framework_state: bstack1lll1ll11l1_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        ob = bstack1lll1l1l11l_opy_(ctx, self.bstack1ll11ll1l1l_opy_, self.bstack1ll11l1l111_opy_, test_framework_state)
        TestFramework.bstack1ll11ll1111_opy_(ob, {
            TestFramework.bstack1llll11111l_opy_: context.test_framework_name,
            TestFramework.bstack1lll11l1ll1_opy_: context.test_framework_version,
            TestFramework.bstack1ll11l1l11l_opy_: [],
            bstack1l11lll1111_opy_.bstack1ll111l1l11_opy_: {},
            bstack1l11lll1111_opy_.bstack1ll11lll11l_opy_: {},
            bstack1l11lll1111_opy_.bstack1ll1111l111_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1l1l11_opy_(ob, TestFramework.bstack1ll11l111l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1l1l11_opy_(ob, TestFramework.bstack1llll1lll11_opy_, context.platform_index)
        TestFramework.bstack1lll11l11ll_opy_[ctx.id] = ob
        self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡦࡸࡽ࠴ࡩࡥ࠿ࡾࡧࡹࡾ࠮ࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣᗽ") + str(TestFramework.bstack1lll11l11ll_opy_.keys()) + bstack11l11ll_opy_ (u"ࠤࠥᗾ"))
        return ob
    def bstack1ll11lll111_opy_(self, instance: bstack1lll1l1l11l_opy_, bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_]):
        bstack1l1llll1111_opy_ = (
            bstack1l11lll1111_opy_.bstack1ll1l1111l1_opy_
            if bstack1llll1ll1l1_opy_[1] == bstack1lll1l1llll_opy_.PRE
            else bstack1l11lll1111_opy_.bstack1ll11l11l1l_opy_
        )
        hook = bstack1l11lll1111_opy_.bstack1ll1l11l111_opy_(instance, bstack1l1llll1111_opy_)
        entries = hook.get(TestFramework.bstack1l1llll1l11_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11l1l11l_opy_, []))
        return entries
    def bstack1ll11ll11ll_opy_(self, instance: bstack1lll1l1l11l_opy_, bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_]):
        bstack1l1llll1111_opy_ = (
            bstack1l11lll1111_opy_.bstack1ll1l1111l1_opy_
            if bstack1llll1ll1l1_opy_[1] == bstack1lll1l1llll_opy_.PRE
            else bstack1l11lll1111_opy_.bstack1ll11l11l1l_opy_
        )
        bstack1l11lll1111_opy_.bstack1ll1l1l11l1_opy_(instance, bstack1l1llll1111_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11l1l11l_opy_, []).clear()
    def bstack1ll11ll111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11l11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡴࡲࡧࡪࡹࡳࡦࡵࠣࡸ࡭࡫ࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡵ࡬ࡱ࡮ࡲࡡࡳࠢࡷࡳࠥࡺࡨࡦࠢࡍࡥࡻࡧࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡯ࡳࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡄࡪࡨࡧࡰࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࡭ࡳࡹࡩࡥࡧࠣࢂ࠴࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠴࡛ࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡊࡴࡸࠠࡦࡣࡦ࡬ࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠮ࠣࡶࡪࡶ࡬ࡢࡥࡨࡷࠥࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧࠦࡩ࡯ࠢ࡬ࡸࡸࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡍ࡫ࠦࡡࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡰࡥࡹࡩࡨࡦࡵࠣࡥࠥࡳ࡯ࡥ࡫ࡩ࡭ࡪࡪࠠࡩࡱࡲ࡯࠲ࡲࡥࡷࡧ࡯ࠤ࡫࡯࡬ࡦ࠮ࠣ࡭ࡹࠦࡣࡳࡧࡤࡸࡪࡹࠠࡢࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࠤࡼ࡯ࡴࡩࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡤࡦࡶࡤ࡭ࡱࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡓࡪ࡯࡬ࡰࡦࡸ࡬ࡺ࠮ࠣ࡭ࡹࠦࡰࡳࡱࡦࡩࡸࡹࡥࡴࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡱࡵࡣࡢࡶࡨࡨࠥ࡯࡮ࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡦࡾࠦࡲࡦࡲ࡯ࡥࡨ࡯࡮ࡨࠢࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢࠡࡹ࡬ࡸ࡭ࠦࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡗ࡬ࡪࠦࡣࡳࡧࡤࡸࡪࡪࠠࡍࡱࡪࡉࡳࡺࡲࡺࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡥࡷ࡫ࠠࡢࡦࡧࡩࡩࠦࡴࡰࠢࡷ࡬ࡪࠦࡨࡰࡱ࡮ࠫࡸࠦࠢ࡭ࡱࡪࡷࠧࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡬ࡴࡵ࡫࠻ࠢࡗ࡬ࡪࠦࡥࡷࡧࡱࡸࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࠦࡡ࡯ࡦࠣ࡬ࡴࡵ࡫ࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤ࡙࡫ࡳࡵࡎࡨࡺࡪࡲࠠ࡮ࡱࡱ࡭ࡹࡵࡲࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡺ࡯࡬ࡥࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠ࡮ࡱࡱ࡭ࡹࡵࡲࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᗿ")
        global _1ll1l11l1ll_opy_
        platform_index = os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᘀ")]
        bstack1ll1l111111_opy_ = os.path.join(bstack1ll11l1l1l1_opy_, (bstack1ll11111lll_opy_ + str(platform_index)), bstack11llll11111_opy_)
        if not os.path.exists(bstack1ll1l111111_opy_) or not os.path.isdir(bstack1ll1l111111_opy_):
            self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡊࡩࡳࡧࡦࡸࡴࡸࡹࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵࡵࠣࡸࡴࠦࡰࡳࡱࡦࡩࡸࡹࠠࡼࡿࠥᘁ").format(bstack1ll1l111111_opy_))
            return
        logs = hook.get(bstack11l11ll_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᘂ"), [])
        with os.scandir(bstack1ll1l111111_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l11l1ll_opy_:
                    self.logger.info(bstack11l11ll_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧᘃ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11l11ll_opy_ (u"ࠣࠤᘄ")
                    log_entry = bstack1ll1l1l1l11_opy_(
                        kind=bstack11l11ll_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᘅ"),
                        message=bstack11l11ll_opy_ (u"ࠥࠦᘆ"),
                        level=bstack11l11ll_opy_ (u"ࠦࠧᘇ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll1l11ll11_opy_=entry.stat().st_size,
                        bstack1ll1l11l1l1_opy_=bstack11l11ll_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧᘈ"),
                        bstack11lll1_opy_=os.path.abspath(entry.path),
                        bstack1ll11lll1ll_opy_=hook.get(TestFramework.bstack1ll11llll11_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l11l1ll_opy_.add(abs_path)
        platform_index = os.environ[bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᘉ")]
        bstack1l1lllllll1_opy_ = os.path.join(bstack1ll11l1l1l1_opy_, (bstack1ll11111lll_opy_ + str(platform_index)), bstack11llll11111_opy_, bstack11lll1llll1_opy_)
        if not os.path.exists(bstack1l1lllllll1_opy_) or not os.path.isdir(bstack1l1lllllll1_opy_):
            self.logger.info(bstack11l11ll_opy_ (u"ࠢࡏࡱࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡪࡴࡻ࡮ࡥࠢࡤࡸ࠿ࠦࡻࡾࠤᘊ").format(bstack1l1lllllll1_opy_))
        else:
            self.logger.info(bstack11l11ll_opy_ (u"ࠣࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡩࡶࡴࡳࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠽ࠤࢀࢃࠢᘋ").format(bstack1l1lllllll1_opy_))
            with os.scandir(bstack1l1lllllll1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l11l1ll_opy_:
                        self.logger.info(bstack11l11ll_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢᘌ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11l11ll_opy_ (u"ࠥࠦᘍ")
                        log_entry = bstack1ll1l1l1l11_opy_(
                            kind=bstack11l11ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᘎ"),
                            message=bstack11l11ll_opy_ (u"ࠧࠨᘏ"),
                            level=bstack11l11ll_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᘐ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll1l11ll11_opy_=entry.stat().st_size,
                            bstack1ll1l11l1l1_opy_=bstack11l11ll_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᘑ"),
                            bstack11lll1_opy_=os.path.abspath(entry.path),
                            bstack1ll1111lll1_opy_=hook.get(TestFramework.bstack1ll11llll11_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l11l1ll_opy_.add(abs_path)
        hook[bstack11l11ll_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᘒ")] = logs
    def bstack1ll11l1ll11_opy_(
        self,
        bstack1ll1111ll11_opy_: bstack1lll1l1l11l_opy_,
        entries: List[bstack1ll1l1l1l11_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11l11ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡖࡉࡘ࡙ࡉࡐࡐࡢࡍࡉࠨᘓ"))
        req.platform_index = TestFramework.get_state(bstack1ll1111ll11_opy_, TestFramework.bstack1llll1lll11_opy_)
        req.execution_context.hash = str(bstack1ll1111ll11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1111ll11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1111ll11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1111ll11_opy_, TestFramework.bstack1llll11111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1111ll11_opy_, TestFramework.bstack1lll11l1ll1_opy_)
            log_entry.uuid = entry.bstack1ll11lll1ll_opy_
            log_entry.test_framework_state = bstack1ll1111ll11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l11ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᘔ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack11l11ll_opy_ (u"ࠦࠧᘕ")
            if entry.kind == bstack11l11ll_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᘖ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l11ll11_opy_
                log_entry.file_path = entry.bstack11lll1_opy_
        def bstack1ll111lllll_opy_():
            bstack1lll1l1l11_opy_ = datetime.now()
            try:
                self.bstack1llll1l1ll1_opy_.LogCreatedEvent(req)
                bstack1ll1111ll11_opy_.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥᘗ"), datetime.now() - bstack1lll1l1l11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l11ll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡿࢂࠨᘘ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l11l1_opy_.enqueue(bstack1ll111lllll_opy_)
    def __1ll111ll11l_opy_(self, instance) -> None:
        bstack11l11ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡒ࡯ࡢࡦࡶࠤࡨࡻࡳࡵࡱࡰࠤࡹࡧࡧࡴࠢࡩࡳࡷࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡨ࡮ࡩࡴࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡰࡪࡼࡥ࡭ࠢࡦࡹࡸࡺ࡯࡮ࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡧࡴࡲࡱࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡶࡵࡷࡳࡲ࡚ࡡࡨࡏࡤࡲࡦ࡭ࡥࡳࠢࡤࡲࡩࠦࡵࡱࡦࡤࡸࡪࡹࠠࡵࡪࡨࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡳࡵࡣࡷࡩࠥࡻࡳࡪࡰࡪࠤࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࡟ࡦࡰࡷࡶ࡮࡫ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᘙ")
        bstack1ll1111111l_opy_ = {bstack11l11ll_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡡࡰࡩࡹࡧࡤࡢࡶࡤࠦᘚ"): bstack1ll11l1llll_opy_.bstack1l1lllll111_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll11ll1111_opy_(instance, bstack1ll1111111l_opy_)
    @staticmethod
    def bstack1ll1l11l111_opy_(instance: bstack1lll1l1l11l_opy_, bstack1l1llll1111_opy_: str):
        bstack1l1llll11l1_opy_ = (
            bstack1l11lll1111_opy_.bstack1ll11lll11l_opy_
            if bstack1l1llll1111_opy_ == bstack1l11lll1111_opy_.bstack1ll11l11l1l_opy_
            else bstack1l11lll1111_opy_.bstack1ll1111l111_opy_
        )
        bstack1ll11l1ll1l_opy_ = TestFramework.get_state(instance, bstack1l1llll1111_opy_, None)
        bstack1l1llll1lll_opy_ = TestFramework.get_state(instance, bstack1l1llll11l1_opy_, None) if bstack1ll11l1ll1l_opy_ else None
        return (
            bstack1l1llll1lll_opy_[bstack1ll11l1ll1l_opy_][-1]
            if isinstance(bstack1l1llll1lll_opy_, dict) and len(bstack1l1llll1lll_opy_.get(bstack1ll11l1ll1l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1l1l11l1_opy_(instance: bstack1lll1l1l11l_opy_, bstack1l1llll1111_opy_: str):
        hook = bstack1l11lll1111_opy_.bstack1ll1l11l111_opy_(instance, bstack1l1llll1111_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1l1llll1l11_opy_, []).clear()
    @staticmethod
    def __1ll1111ll1l_opy_(instance: bstack1lll1l1l11l_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l11ll_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡦࡳࡷࡪࡳࠣᘛ"), None)):
            return
        if os.getenv(bstack11l11ll_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡐࡔࡍࡓࠣᘜ"), bstack11l11ll_opy_ (u"ࠧ࠷ࠢᘝ")) != bstack11l11ll_opy_ (u"ࠨ࠱ࠣᘞ"):
            bstack1l11lll1111_opy_.logger.warning(bstack11l11ll_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡯࡮ࡨࠢࡦࡥࡵࡲ࡯ࡨࠤᘟ"))
            return
        bstack1l1llllllll_opy_ = {
            bstack11l11ll_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢᘠ"): (bstack1l11lll1111_opy_.bstack1ll1l1111l1_opy_, bstack1l11lll1111_opy_.bstack1ll1111l111_opy_),
            bstack11l11ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᘡ"): (bstack1l11lll1111_opy_.bstack1ll11l11l1l_opy_, bstack1l11lll1111_opy_.bstack1ll11lll11l_opy_),
        }
        for when in (bstack11l11ll_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᘢ"), bstack11l11ll_opy_ (u"ࠦࡨࡧ࡬࡭ࠤᘣ"), bstack11l11ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢᘤ")):
            bstack1l1lll1ll1l_opy_ = args[1].get_records(when)
            if not bstack1l1lll1ll1l_opy_:
                continue
            records = [
                bstack1ll1l1l1l11_opy_(
                    kind=TestFramework.bstack1ll111l1111_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l11ll_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠤᘥ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l11ll_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࠣᘦ")) and r.created
                        else None
                    ),
                )
                for r in bstack1l1lll1ll1l_opy_
                if isinstance(getattr(r, bstack11l11ll_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤᘧ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11llll1l_opy_, bstack1l1llll11l1_opy_ = bstack1l1llllllll_opy_.get(when, (None, None))
            bstack1l1lll1l11l_opy_ = TestFramework.get_state(instance, bstack1ll11llll1l_opy_, None) if bstack1ll11llll1l_opy_ else None
            bstack1l1llll1lll_opy_ = TestFramework.get_state(instance, bstack1l1llll11l1_opy_, None) if bstack1l1lll1l11l_opy_ else None
            if isinstance(bstack1l1llll1lll_opy_, dict) and len(bstack1l1llll1lll_opy_.get(bstack1l1lll1l11l_opy_, [])) > 0:
                hook = bstack1l1llll1lll_opy_[bstack1l1lll1l11l_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1l1llll1l11_opy_ in hook:
                    hook[TestFramework.bstack1l1llll1l11_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11l1l11l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1l1llll1ll1_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l11lll1111_opy_.__1l1llll11ll_opy_(test.location) if hasattr(test, bstack11l11ll_opy_ (u"ࠤ࡯ࡳࡨࡧࡴࡪࡱࡱࠦᘨ")) else getattr(test, bstack11l11ll_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᘩ"), None)
        test_name = test.name if hasattr(test, bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᘪ")) else None
        bstack1ll1l1111ll_opy_ = test.fspath.strpath if hasattr(test, bstack11l11ll_opy_ (u"ࠧ࡬ࡳࡱࡣࡷ࡬ࠧᘫ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll1l1111ll_opy_:
            return None
        code = None
        if hasattr(test, bstack11l11ll_opy_ (u"ࠨ࡯ࡣ࡬ࠥᘬ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11lll1lllll_opy_ = []
        try:
            bstack11lll1lllll_opy_ = bstack1l1l111l_opy_.bstack1l111l1l_opy_(test)
        except:
            bstack1l11lll1111_opy_.logger.warning(bstack11l11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡶࡨࡷࡹࠦࡳࡤࡱࡳࡩࡸ࠲ࠠࡵࡧࡶࡸࠥࡹࡣࡰࡲࡨࡷࠥࡽࡩ࡭࡮ࠣࡦࡪࠦࡲࡦࡵࡲࡰࡻ࡫ࡤࠡ࡫ࡱࠤࡈࡒࡉࠣᘭ"))
        return {
            TestFramework.bstack1lll11l1lll_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l111l1l_opy_: test_id,
            TestFramework.bstack1l1lll1llll_opy_: test_name,
            TestFramework.bstack1ll1l11111l_opy_: getattr(test, bstack11l11ll_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᘮ"), None),
            TestFramework.bstack1ll111llll1_opy_: bstack1ll1l1111ll_opy_,
            TestFramework.bstack1ll111l1ll1_opy_: bstack1l11lll1111_opy_.__1ll111ll111_opy_(test),
            TestFramework.bstack1ll11llllll_opy_: code,
            TestFramework.bstack1lll11l1l11_opy_: TestFramework.bstack1ll1111l1l1_opy_,
            TestFramework.bstack1lll111llll_opy_: test_id,
            TestFramework.bstack1l111111l1l_opy_: bstack11lll1lllll_opy_
        }
    @staticmethod
    def __1ll111ll111_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack11l11ll_opy_ (u"ࠤࡲࡻࡳࡥ࡭ࡢࡴ࡮ࡩࡷࡹࠢᘯ"), [])
            markers.extend([getattr(m, bstack11l11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᘰ"), None) for m in own_markers if getattr(m, bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᘱ"), None)])
            current = getattr(current, bstack11l11ll_opy_ (u"ࠧࡶࡡࡳࡧࡱࡸࠧᘲ"), None)
        return markers
    @staticmethod
    def __1l1llll11ll_opy_(location):
        return bstack11l11ll_opy_ (u"ࠨ࠺࠻ࠤᘳ").join(filter(lambda x: isinstance(x, str), location))