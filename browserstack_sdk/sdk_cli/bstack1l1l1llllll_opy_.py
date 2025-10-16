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
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll111111l_opy_ import bstack1ll1lll11l1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1l11111ll_opy_ import bstack1ll111lll11_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll111l1l_opy_,
    bstack1llll1111ll_opy_,
    bstack1lll1ll111l_opy_,
    bstack1ll111ll1ll_opy_,
    bstack1ll11l111l1_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll11l1l111_opy_
from bstack_utils.bstack11l111l1l_opy_ import bstack1llll1lllll_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll11lllll_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1l111l11_opy_ import bstack1ll1l111lll_opy_
from bstack_utils.bstack1llll1l1_opy_ import bstack1l11l1ll_opy_
bstack1ll111llll1_opy_ = bstack1ll11l1l111_opy_()
bstack1ll111lllll_opy_ = 1.0
bstack1ll11l1ll1l_opy_ = bstack1ll11_opy_ (u"ࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢᕩ")
bstack11llll1llll_opy_ = bstack1ll11_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᕪ")
bstack11llll1l1ll_opy_ = bstack1ll11_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᕫ")
bstack11llll1ll11_opy_ = bstack1ll11_opy_ (u"ࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨᕬ")
bstack11llll1ll1l_opy_ = bstack1ll11_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥᕭ")
_1ll11l11l11_opy_ = set()
class bstack1l1l11lll1l_opy_(TestFramework):
    bstack1ll1l111ll1_opy_ = bstack1ll11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᕮ")
    bstack1ll11l11ll1_opy_ = bstack1ll11_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࠦᕯ")
    bstack1ll1l11l1l1_opy_ = bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᕰ")
    bstack1ll1111l111_opy_ = bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࠥᕱ")
    bstack1l1lllll1l1_opy_ = bstack1ll11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧᕲ")
    bstack1ll111l11ll_opy_: bool
    bstack1lll1l11111_opy_: bstack1lll11lllll_opy_  = None
    bstack1llllll111l_opy_ = None
    bstack1ll11llll11_opy_ = [
        bstack1llll111l1l_opy_.BEFORE_ALL,
        bstack1llll111l1l_opy_.AFTER_ALL,
        bstack1llll111l1l_opy_.BEFORE_EACH,
        bstack1llll111l1l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11ll1l11_opy_: Dict[str, str],
        bstack1ll11l11lll_opy_: List[str]=[bstack1ll11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᕳ")],
        bstack1lll1l11111_opy_: bstack1lll11lllll_opy_=None,
        bstack1llllll111l_opy_=None
    ):
        super().__init__(bstack1ll11l11lll_opy_, bstack1ll11ll1l11_opy_, bstack1lll1l11111_opy_)
        self.bstack1ll111l11ll_opy_ = any(bstack1ll11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᕴ") in item.lower() for item in bstack1ll11l11lll_opy_)
        self.bstack1llllll111l_opy_ = bstack1llllll111l_opy_
    def track_event(
        self,
        context: bstack1ll111ll1ll_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll111l1l_opy_.TEST or test_framework_state in bstack1l1l11lll1l_opy_.bstack1ll11llll11_opy_:
            bstack1ll111lll11_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll111l1l_opy_.NONE:
            self.logger.warning(bstack1ll11_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࠨᕵ") + str(test_hook_state) + bstack1ll11_opy_ (u"ࠨࠢᕶ"))
            return
        if not self.bstack1ll111l11ll_opy_:
            self.logger.warning(bstack1ll11_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠽ࠣᕷ") + str(str(self.bstack1ll11l11lll_opy_)) + bstack1ll11_opy_ (u"ࠣࠤᕸ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1ll11_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᕹ") + str(kwargs) + bstack1ll11_opy_ (u"ࠥࠦᕺ"))
            return
        instance = self.__1ll1l1111l1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1ll11_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡦࡸࡧࡴ࠿ࠥᕻ") + str(args) + bstack1ll11_opy_ (u"ࠧࠨᕼ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l1l11lll1l_opy_.bstack1ll11llll11_opy_ and test_hook_state == bstack1lll1ll111l_opy_.PRE:
                bstack1ll1l1ll1l1_opy_ = bstack1llll1lllll_opy_.bstack1ll111lll1l_opy_(EVENTS.bstack1ll1ll1l1_opy_.value)
                name = str(EVENTS.bstack1ll1ll1l1_opy_.name)+bstack1ll11_opy_ (u"ࠨ࠺ࠣᕽ")+str(test_framework_state.name)
                TestFramework.bstack1ll11lllll1_opy_(instance, name, bstack1ll1l1ll1l1_opy_)
        except Exception as e:
            self.logger.debug(bstack1ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴࠣࡴࡷ࡫࠺ࠡࡽࢀࠦᕾ").format(e))
        try:
            if not TestFramework.bstack1111111lll_opy_(instance, TestFramework.bstack1ll11ll111l_opy_) and test_hook_state == bstack1lll1ll111l_opy_.PRE:
                test = bstack1l1l11lll1l_opy_.__1ll11ll11l1_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1ll11_opy_ (u"ࠣ࡮ࡲࡥࡩ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᕿ") + str(test_hook_state) + bstack1ll11_opy_ (u"ࠤࠥᖀ"))
            if test_framework_state == bstack1llll111l1l_opy_.TEST:
                if test_hook_state == bstack1lll1ll111l_opy_.PRE and not TestFramework.bstack1111111lll_opy_(instance, TestFramework.bstack1ll11lll111_opy_):
                    TestFramework.bstack1llll1ll1ll_opy_(instance, TestFramework.bstack1ll11lll111_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1ll11_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲ࡹࡴࡢࡴࡷࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᖁ") + str(test_hook_state) + bstack1ll11_opy_ (u"ࠦࠧᖂ"))
                elif test_hook_state == bstack1lll1ll111l_opy_.POST and not TestFramework.bstack1111111lll_opy_(instance, TestFramework.bstack1ll1l1l1ll1_opy_):
                    TestFramework.bstack1llll1ll1ll_opy_(instance, TestFramework.bstack1ll1l1l1ll1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1ll11_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡦࡰࡧࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᖃ") + str(test_hook_state) + bstack1ll11_opy_ (u"ࠨࠢᖄ"))
            elif test_framework_state == bstack1llll111l1l_opy_.LOG and test_hook_state == bstack1lll1ll111l_opy_.POST:
                bstack1l1l11lll1l_opy_.__1ll1111111l_opy_(instance, *args)
            elif test_framework_state == bstack1llll111l1l_opy_.LOG_REPORT and test_hook_state == bstack1lll1ll111l_opy_.POST:
                self.__1ll11l11111_opy_(instance, *args)
                self.__1l1lllll1ll_opy_(instance)
            elif test_framework_state in bstack1l1l11lll1l_opy_.bstack1ll11llll11_opy_:
                self.__1ll11lll1ll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1ll11_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᖅ") + str(instance.ref()) + bstack1ll11_opy_ (u"ࠣࠤᖆ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l1llllll11_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l1l11lll1l_opy_.bstack1ll11llll11_opy_ and test_hook_state == bstack1lll1ll111l_opy_.POST:
                name = str(EVENTS.bstack1ll1ll1l1_opy_.name)+bstack1ll11_opy_ (u"ࠤ࠽ࠦᖇ")+str(test_framework_state.name)
                bstack1ll1l1ll1l1_opy_ = TestFramework.bstack1ll1l11llll_opy_(instance, name)
                bstack1llll1lllll_opy_.end(EVENTS.bstack1ll1ll1l1_opy_.value, bstack1ll1l1ll1l1_opy_+bstack1ll11_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᖈ"), bstack1ll1l1ll1l1_opy_+bstack1ll11_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᖉ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1ll11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᖊ").format(e))
    def bstack1ll11ll1ll1_opy_(self):
        return self.bstack1ll111l11ll_opy_
    def __1ll111111ll_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1ll11_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥᖋ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11lll1l1_opy_(rep, [bstack1ll11_opy_ (u"ࠢࡸࡪࡨࡲࠧᖌ"), bstack1ll11_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᖍ"), bstack1ll11_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤᖎ"), bstack1ll11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᖏ"), bstack1ll11_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠧᖐ"), bstack1ll11_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦᖑ")])
        return None
    def __1ll11l11111_opy_(self, instance: bstack1llll1111ll_opy_, *args):
        result = self.__1ll111111ll_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l111l_opy_ = None
        if result.get(bstack1ll11_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᖒ"), None) == bstack1ll11_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᖓ") and len(args) > 1 and getattr(args[1], bstack1ll11_opy_ (u"ࠣࡧࡻࡧ࡮ࡴࡦࡰࠤᖔ"), None) is not None:
            failure = [{bstack1ll11_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᖕ"): [args[1].excinfo.exconly(), result.get(bstack1ll11_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤᖖ"), None)]}]
            bstack11111l111l_opy_ = bstack1ll11_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧᖗ") if bstack1ll11_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᖘ") in getattr(args[1].excinfo, bstack1ll11_opy_ (u"ࠨࡴࡺࡲࡨࡲࡦࡳࡥࠣᖙ"), bstack1ll11_opy_ (u"ࠢࠣᖚ")) else bstack1ll11_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᖛ")
        bstack1ll11111lll_opy_ = result.get(bstack1ll11_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᖜ"), TestFramework.bstack1ll1ll111ll_opy_)
        if bstack1ll11111lll_opy_ != TestFramework.bstack1ll1ll111ll_opy_:
            TestFramework.bstack1llll1ll1ll_opy_(instance, TestFramework.bstack1l1lllll111_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11l1l11l_opy_(instance, {
            TestFramework.bstack1llll11l11l_opy_: failure,
            TestFramework.bstack1ll1l1l1111_opy_: bstack11111l111l_opy_,
            TestFramework.bstack1lll1llll1l_opy_: bstack1ll11111lll_opy_,
        })
    def __1ll1l1111l1_opy_(
        self,
        context: bstack1ll111ll1ll_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll111l1l_opy_.SETUP_FIXTURE:
            instance = self.__1ll111111l1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1l1ll111_opy_ bstack1ll1l1lll1l_opy_ this to be bstack1ll11_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᖝ")
            if test_framework_state == bstack1llll111l1l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1111lll1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll111l1l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1ll11_opy_ (u"ࠦࡳࡵࡤࡦࠤᖞ"), None), bstack1ll11_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᖟ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1ll11_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᖠ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll1l1lllll_opy_(target) if target else None
        return instance
    def __1ll11lll1ll_opy_(
        self,
        instance: bstack1llll1111ll_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l1l1l11_opy_ = TestFramework.get_state(instance, bstack1l1l11lll1l_opy_.bstack1ll11l11ll1_opy_, {})
        if not key in bstack1ll1l1l1l11_opy_:
            bstack1ll1l1l1l11_opy_[key] = []
        bstack1ll11l1llll_opy_ = TestFramework.get_state(instance, bstack1l1l11lll1l_opy_.bstack1ll1l11l1l1_opy_, {})
        if not key in bstack1ll11l1llll_opy_:
            bstack1ll11l1llll_opy_[key] = []
        bstack1ll11l1l1ll_opy_ = {
            bstack1l1l11lll1l_opy_.bstack1ll11l11ll1_opy_: bstack1ll1l1l1l11_opy_,
            bstack1l1l11lll1l_opy_.bstack1ll1l11l1l1_opy_: bstack1ll11l1llll_opy_,
        }
        if test_hook_state == bstack1lll1ll111l_opy_.PRE:
            hook = {
                bstack1ll11_opy_ (u"ࠢ࡬ࡧࡼࠦᖡ"): key,
                TestFramework.bstack1ll1111l11l_opy_: uuid4().__str__(),
                TestFramework.bstack1ll1l11l1ll_opy_: TestFramework.bstack1ll1l1l1lll_opy_,
                TestFramework.bstack1ll1l1lll11_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l111ll_opy_: [],
                TestFramework.bstack1ll11ll1111_opy_: args[1] if len(args) > 1 else bstack1ll11_opy_ (u"ࠨࠩᖢ"),
                TestFramework.bstack1ll1l1l11ll_opy_: bstack1ll1l111lll_opy_.bstack1ll1l11ll11_opy_()
            }
            bstack1ll1l1l1l11_opy_[key].append(hook)
            bstack1ll11l1l1ll_opy_[bstack1l1l11lll1l_opy_.bstack1ll1111l111_opy_] = key
        elif test_hook_state == bstack1lll1ll111l_opy_.POST:
            bstack1ll1111ll11_opy_ = bstack1ll1l1l1l11_opy_.get(key, [])
            hook = bstack1ll1111ll11_opy_.pop() if bstack1ll1111ll11_opy_ else None
            if hook:
                result = self.__1ll111111ll_opy_(*args)
                if result:
                    bstack1l1lllll11l_opy_ = result.get(bstack1ll11_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᖣ"), TestFramework.bstack1ll1l1l1lll_opy_)
                    if bstack1l1lllll11l_opy_ != TestFramework.bstack1ll1l1l1lll_opy_:
                        hook[TestFramework.bstack1ll1l11l1ll_opy_] = bstack1l1lllll11l_opy_
                hook[TestFramework.bstack1ll1l111111_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l1l11ll_opy_]= bstack1ll1l111lll_opy_.bstack1ll1l11ll11_opy_()
                self.bstack1ll11l11l1l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11111111_opy_, [])
                if logs: self.bstack1ll1l1ll11l_opy_(instance, logs)
                bstack1ll11l1llll_opy_[key].append(hook)
                bstack1ll11l1l1ll_opy_[bstack1l1l11lll1l_opy_.bstack1l1lllll1l1_opy_] = key
        TestFramework.bstack1ll11l1l11l_opy_(instance, bstack1ll11l1l1ll_opy_)
        self.logger.debug(bstack1ll11_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡ࡫ࡳࡴࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾ࡯ࡪࡿࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࡂࢁࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࢃࠠࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤ࠾ࠤᖤ") + str(bstack1ll11l1llll_opy_) + bstack1ll11_opy_ (u"ࠦࠧᖥ"))
    def __1ll111111l1_opy_(
        self,
        context: bstack1ll111ll1ll_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11lll1l1_opy_(args[0], [bstack1ll11_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᖦ"), bstack1ll11_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢᖧ"), bstack1ll11_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢᖨ"), bstack1ll11_opy_ (u"ࠣ࡫ࡧࡷࠧᖩ"), bstack1ll11_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦᖪ"), bstack1ll11_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥᖫ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1ll11_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᖬ")) else fixturedef.get(bstack1ll11_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᖭ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1ll11_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦᖮ")) else None
        node = request.node if hasattr(request, bstack1ll11_opy_ (u"ࠢ࡯ࡱࡧࡩࠧᖯ")) else None
        target = request.node.nodeid if hasattr(node, bstack1ll11_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᖰ")) else None
        baseid = fixturedef.get(bstack1ll11_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤᖱ"), None) or bstack1ll11_opy_ (u"ࠥࠦᖲ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1ll11_opy_ (u"ࠦࡤࡶࡹࡧࡷࡱࡧ࡮ࡺࡥ࡮ࠤᖳ")):
            target = bstack1l1l11lll1l_opy_.__1ll11l1ll11_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1ll11_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢᖴ")) else None
            if target and not TestFramework.bstack1ll1l1lllll_opy_(target):
                self.__1ll1111lll1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1ll11_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡰࡲࡨࡪࡃࡻ࡯ࡱࡧࡩࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᖵ") + str(test_hook_state) + bstack1ll11_opy_ (u"ࠢࠣᖶ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1ll11_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࡃࡻࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨᖷ") + str(target) + bstack1ll11_opy_ (u"ࠤࠥᖸ"))
            return None
        instance = TestFramework.bstack1ll1l1lllll_opy_(target)
        if not instance:
            self.logger.warning(bstack1ll11_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡥࡥࡸ࡫ࡩࡥ࠿ࡾࡦࡦࡹࡥࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧᖹ") + str(target) + bstack1ll11_opy_ (u"ࠦࠧᖺ"))
            return None
        bstack1ll111l1l1l_opy_ = TestFramework.get_state(instance, bstack1l1l11lll1l_opy_.bstack1ll1l111ll1_opy_, {})
        if os.getenv(bstack1ll11_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡋࡏࡘࡕࡗࡕࡉࡘࠨᖻ"), bstack1ll11_opy_ (u"ࠨ࠱ࠣᖼ")) == bstack1ll11_opy_ (u"ࠢ࠲ࠤᖽ"):
            bstack1ll11111l1l_opy_ = bstack1ll11_opy_ (u"ࠣ࠼ࠥᖾ").join((scope, fixturename))
            bstack1l1llllllll_opy_ = datetime.now(tz=timezone.utc)
            bstack1l1llllll1l_opy_ = {
                bstack1ll11_opy_ (u"ࠤ࡮ࡩࡾࠨᖿ"): bstack1ll11111l1l_opy_,
                bstack1ll11_opy_ (u"ࠥࡸࡦ࡭ࡳࠣᗀ"): bstack1l1l11lll1l_opy_.__1ll111ll1l1_opy_(request.node),
                bstack1ll11_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࠧᗁ"): fixturedef,
                bstack1ll11_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗂ"): scope,
                bstack1ll11_opy_ (u"ࠨࡴࡺࡲࡨࠦᗃ"): None,
            }
            try:
                if test_hook_state == bstack1lll1ll111l_opy_.POST and callable(getattr(args[-1], bstack1ll11_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᗄ"), None)):
                    bstack1l1llllll1l_opy_[bstack1ll11_opy_ (u"ࠣࡶࡼࡴࡪࠨᗅ")] = TestFramework.bstack1ll1111ll1l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1ll111l_opy_.PRE:
                bstack1l1llllll1l_opy_[bstack1ll11_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᗆ")] = uuid4().__str__()
                bstack1l1llllll1l_opy_[bstack1l1l11lll1l_opy_.bstack1ll1l1lll11_opy_] = bstack1l1llllllll_opy_
            elif test_hook_state == bstack1lll1ll111l_opy_.POST:
                bstack1l1llllll1l_opy_[bstack1l1l11lll1l_opy_.bstack1ll1l111111_opy_] = bstack1l1llllllll_opy_
            if bstack1ll11111l1l_opy_ in bstack1ll111l1l1l_opy_:
                bstack1ll111l1l1l_opy_[bstack1ll11111l1l_opy_].update(bstack1l1llllll1l_opy_)
                self.logger.debug(bstack1ll11_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࠦᗇ") + str(bstack1ll111l1l1l_opy_[bstack1ll11111l1l_opy_]) + bstack1ll11_opy_ (u"ࠦࠧᗈ"))
            else:
                bstack1ll111l1l1l_opy_[bstack1ll11111l1l_opy_] = bstack1l1llllll1l_opy_
                self.logger.debug(bstack1ll11_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࡿࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࢀࠤࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࠣᗉ") + str(len(bstack1ll111l1l1l_opy_)) + bstack1ll11_opy_ (u"ࠨࠢᗊ"))
        TestFramework.bstack1llll1ll1ll_opy_(instance, bstack1l1l11lll1l_opy_.bstack1ll1l111ll1_opy_, bstack1ll111l1l1l_opy_)
        self.logger.debug(bstack1ll11_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࡽ࡯ࡩࡳ࠮ࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠫࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᗋ") + str(instance.ref()) + bstack1ll11_opy_ (u"ࠣࠤᗌ"))
        return instance
    def __1ll1111lll1_opy_(
        self,
        context: bstack1ll111ll1ll_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1lll11l1_opy_.create_context(target)
        ob = bstack1llll1111ll_opy_(ctx, self.bstack1ll11l11lll_opy_, self.bstack1ll11ll1l11_opy_, test_framework_state)
        TestFramework.bstack1ll11l1l11l_opy_(ob, {
            TestFramework.bstack1llll111l11_opy_: context.test_framework_name,
            TestFramework.bstack1llll1l1l11_opy_: context.test_framework_version,
            TestFramework.bstack1ll11l1111l_opy_: [],
            bstack1l1l11lll1l_opy_.bstack1ll1l111ll1_opy_: {},
            bstack1l1l11lll1l_opy_.bstack1ll1l11l1l1_opy_: {},
            bstack1l1l11lll1l_opy_.bstack1ll11l11ll1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1ll1ll_opy_(ob, TestFramework.bstack1ll11l1l1l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1ll1ll_opy_(ob, TestFramework.bstack1lllll111ll_opy_, context.platform_index)
        TestFramework.bstack1llll1111l1_opy_[ctx.id] = ob
        self.logger.debug(bstack1ll11_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡧࡹࡾ࠮ࡪࡦࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᗍ") + str(TestFramework.bstack1llll1111l1_opy_.keys()) + bstack1ll11_opy_ (u"ࠥࠦᗎ"))
        return ob
    def bstack1ll1ll111l1_opy_(self, instance: bstack1llll1111ll_opy_, bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_]):
        bstack1ll11111l11_opy_ = (
            bstack1l1l11lll1l_opy_.bstack1ll1111l111_opy_
            if bstack1llll1l1ll1_opy_[1] == bstack1lll1ll111l_opy_.PRE
            else bstack1l1l11lll1l_opy_.bstack1l1lllll1l1_opy_
        )
        hook = bstack1l1l11lll1l_opy_.bstack1ll1ll1111l_opy_(instance, bstack1ll11111l11_opy_)
        entries = hook.get(TestFramework.bstack1ll11l111ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11l1111l_opy_, []))
        return entries
    def bstack1ll111l1111_opy_(self, instance: bstack1llll1111ll_opy_, bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_]):
        bstack1ll11111l11_opy_ = (
            bstack1l1l11lll1l_opy_.bstack1ll1111l111_opy_
            if bstack1llll1l1ll1_opy_[1] == bstack1lll1ll111l_opy_.PRE
            else bstack1l1l11lll1l_opy_.bstack1l1lllll1l1_opy_
        )
        bstack1l1l11lll1l_opy_.bstack1ll111l1lll_opy_(instance, bstack1ll11111l11_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11l1111l_opy_, []).clear()
    def bstack1ll11l11l1l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1ll11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡶ࡭ࡲ࡯࡬ࡢࡴࠣࡸࡴࠦࡴࡩࡧࠣࡎࡦࡼࡡࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡩࡴࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡅ࡫ࡩࡨࡱࡳࠡࡶ࡫ࡩࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡮ࡴࡳࡪࡦࡨࠤࢃ࠵࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠵ࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠯ࠤࡷ࡫ࡰ࡭ࡣࡦࡩࡸࠦࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥࠤࡼ࡯ࡴࡩࠢࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨࠠࡪࡰࠣ࡭ࡹࡹࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡎ࡬ࠠࡢࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣࡸ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡱࡦࡺࡣࡩࡧࡶࠤࡦࠦ࡭ࡰࡦ࡬ࡪ࡮࡫ࡤࠡࡪࡲࡳࡰ࠳࡬ࡦࡸࡨࡰࠥ࡬ࡩ࡭ࡧ࠯ࠤ࡮ࡺࠠࡤࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡐࡴ࡭ࡅ࡯ࡶࡵࡽࠥࡵࡢ࡫ࡧࡦࡸࠥࡽࡩࡵࡪࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡔ࡫ࡰ࡭ࡱࡧࡲ࡭ࡻ࠯ࠤ࡮ࡺࠠࡱࡴࡲࡧࡪࡹࡳࡦࡵࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡲ࡯ࡤࡣࡷࡩࡩࠦࡩ࡯ࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡧࡿࠠࡳࡧࡳࡰࡦࡩࡩ࡯ࡩࠣࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡘ࡭࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࡶࠤࡦࡸࡥࠡࡣࡧࡨࡪࡪࠠࡵࡱࠣࡸ࡭࡫ࠠࡩࡱࡲ࡯ࠬࡹࠠࠣ࡮ࡲ࡫ࡸࠨࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬࠼ࠣࡘ࡭࡫ࠠࡦࡸࡨࡲࡹࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹࠠࡢࡰࡧࠤ࡭ࡵ࡯࡬ࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩ࡚ࠥࡥࡴࡶࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡻࡩ࡭ࡦࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᗏ")
        global _1ll11l11l11_opy_
        platform_index = os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᗐ")]
        bstack1ll11l1lll1_opy_ = os.path.join(bstack1ll111llll1_opy_, (bstack1ll11l1ll1l_opy_ + str(platform_index)), bstack11llll1ll11_opy_)
        if not os.path.exists(bstack1ll11l1lll1_opy_) or not os.path.isdir(bstack1ll11l1lll1_opy_):
            self.logger.debug(bstack1ll11_opy_ (u"ࠨࡄࡪࡴࡨࡧࡹࡵࡲࡺࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶࡶࠤࡹࡵࠠࡱࡴࡲࡧࡪࡹࡳࠡࡽࢀࠦᗑ").format(bstack1ll11l1lll1_opy_))
            return
        logs = hook.get(bstack1ll11_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᗒ"), [])
        with os.scandir(bstack1ll11l1lll1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l11l11_opy_:
                    self.logger.info(bstack1ll11_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᗓ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1ll11_opy_ (u"ࠤࠥᗔ")
                    log_entry = bstack1ll11l111l1_opy_(
                        kind=bstack1ll11_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᗕ"),
                        message=bstack1ll11_opy_ (u"ࠦࠧᗖ"),
                        level=bstack1ll11_opy_ (u"ࠧࠨᗗ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll1l1l1l1l_opy_=entry.stat().st_size,
                        bstack1l1lllllll1_opy_=bstack1ll11_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᗘ"),
                        bstack1lll111_opy_=os.path.abspath(entry.path),
                        bstack1ll111l11l1_opy_=hook.get(TestFramework.bstack1ll1111l11l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l11l11_opy_.add(abs_path)
        platform_index = os.environ[bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᗙ")]
        bstack1ll1l1l11l1_opy_ = os.path.join(bstack1ll111llll1_opy_, (bstack1ll11l1ll1l_opy_ + str(platform_index)), bstack11llll1ll11_opy_, bstack11llll1ll1l_opy_)
        if not os.path.exists(bstack1ll1l1l11l1_opy_) or not os.path.isdir(bstack1ll1l1l11l1_opy_):
            self.logger.info(bstack1ll11_opy_ (u"ࠣࡐࡲࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣࡥࡹࡀࠠࡼࡿࠥᗚ").format(bstack1ll1l1l11l1_opy_))
        else:
            self.logger.info(bstack1ll11_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡪࡷࡵ࡭ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣᗛ").format(bstack1ll1l1l11l1_opy_))
            with os.scandir(bstack1ll1l1l11l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l11l11_opy_:
                        self.logger.info(bstack1ll11_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᗜ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1ll11_opy_ (u"ࠦࠧᗝ")
                        log_entry = bstack1ll11l111l1_opy_(
                            kind=bstack1ll11_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᗞ"),
                            message=bstack1ll11_opy_ (u"ࠨࠢᗟ"),
                            level=bstack1ll11_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᗠ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll1l1l1l1l_opy_=entry.stat().st_size,
                            bstack1l1lllllll1_opy_=bstack1ll11_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᗡ"),
                            bstack1lll111_opy_=os.path.abspath(entry.path),
                            bstack1ll11llllll_opy_=hook.get(TestFramework.bstack1ll1111l11l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l11l11_opy_.add(abs_path)
        hook[bstack1ll11_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᗢ")] = logs
    def bstack1ll1l1ll11l_opy_(
        self,
        bstack1ll11ll1lll_opy_: bstack1llll1111ll_opy_,
        entries: List[bstack1ll11l111l1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1ll11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢᗣ"))
        req.platform_index = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1lllll111ll_opy_)
        req.execution_context.hash = str(bstack1ll11ll1lll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11ll1lll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11ll1lll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1llll111l11_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1llll1l1l11_opy_)
            log_entry.uuid = entry.bstack1ll111l11l1_opy_
            log_entry.test_framework_state = bstack1ll11ll1lll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1ll11_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᗤ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1ll11_opy_ (u"ࠧࠨᗥ")
            if entry.kind == bstack1ll11_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᗦ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1l1l1l_opy_
                log_entry.file_path = entry.bstack1lll111_opy_
        def bstack1ll111l1l11_opy_():
            bstack11l1lll1l_opy_ = datetime.now()
            try:
                self.bstack1llllll111l_opy_.LogCreatedEvent(req)
                bstack1ll11ll1lll_opy_.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦᗧ"), datetime.now() - bstack11l1lll1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1ll11_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࢀࢃࠢᗨ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll111l1l11_opy_)
    def __1l1lllll1ll_opy_(self, instance) -> None:
        bstack1ll11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡌࡰࡣࡧࡷࠥࡩࡵࡴࡶࡲࡱࠥࡺࡡࡨࡵࠣࡪࡴࡸࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡵࡩࡦࡺࡥࡴࠢࡤࠤࡩ࡯ࡣࡵࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡱ࡫ࡶࡦ࡮ࠣࡧࡺࡹࡴࡰ࡯ࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࡤࠡࡨࡵࡳࡲࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡷࡶࡸࡴࡳࡔࡢࡩࡐࡥࡳࡧࡧࡦࡴࠣࡥࡳࡪࠠࡶࡲࡧࡥࡹ࡫ࡳࠡࡶ࡫ࡩࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡴࡶࡤࡸࡪࠦࡵࡴ࡫ࡱ࡫ࠥࡹࡥࡵࡡࡶࡸࡦࡺࡥࡠࡧࡱࡸࡷ࡯ࡥࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᗩ")
        bstack1ll11l1l1ll_opy_ = {bstack1ll11_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡢࡱࡪࡺࡡࡥࡣࡷࡥࠧᗪ"): bstack1ll1l111lll_opy_.bstack1ll1l11ll11_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll11l1l11l_opy_(instance, bstack1ll11l1l1ll_opy_)
    @staticmethod
    def bstack1ll1ll1111l_opy_(instance: bstack1llll1111ll_opy_, bstack1ll11111l11_opy_: str):
        bstack1ll11llll1l_opy_ = (
            bstack1l1l11lll1l_opy_.bstack1ll1l11l1l1_opy_
            if bstack1ll11111l11_opy_ == bstack1l1l11lll1l_opy_.bstack1l1lllll1l1_opy_
            else bstack1l1l11lll1l_opy_.bstack1ll11l11ll1_opy_
        )
        bstack1ll11ll11ll_opy_ = TestFramework.get_state(instance, bstack1ll11111l11_opy_, None)
        bstack1ll111ll111_opy_ = TestFramework.get_state(instance, bstack1ll11llll1l_opy_, None) if bstack1ll11ll11ll_opy_ else None
        return (
            bstack1ll111ll111_opy_[bstack1ll11ll11ll_opy_][-1]
            if isinstance(bstack1ll111ll111_opy_, dict) and len(bstack1ll111ll111_opy_.get(bstack1ll11ll11ll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll111l1lll_opy_(instance: bstack1llll1111ll_opy_, bstack1ll11111l11_opy_: str):
        hook = bstack1l1l11lll1l_opy_.bstack1ll1ll1111l_opy_(instance, bstack1ll11111l11_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l111ll_opy_, []).clear()
    @staticmethod
    def __1ll1111111l_opy_(instance: bstack1llll1111ll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1ll11_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡧࡴࡸࡤࡴࠤᗫ"), None)):
            return
        if os.getenv(bstack1ll11_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡑࡕࡇࡔࠤᗬ"), bstack1ll11_opy_ (u"ࠨ࠱ࠣᗭ")) != bstack1ll11_opy_ (u"ࠢ࠲ࠤᗮ"):
            bstack1l1l11lll1l_opy_.logger.warning(bstack1ll11_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡩ࡯ࡩࠣࡧࡦࡶ࡬ࡰࡩࠥᗯ"))
            return
        bstack1l1llll1lll_opy_ = {
            bstack1ll11_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᗰ"): (bstack1l1l11lll1l_opy_.bstack1ll1111l111_opy_, bstack1l1l11lll1l_opy_.bstack1ll11l11ll1_opy_),
            bstack1ll11_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᗱ"): (bstack1l1l11lll1l_opy_.bstack1l1lllll1l1_opy_, bstack1l1l11lll1l_opy_.bstack1ll1l11l1l1_opy_),
        }
        for when in (bstack1ll11_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᗲ"), bstack1ll11_opy_ (u"ࠧࡩࡡ࡭࡮ࠥᗳ"), bstack1ll11_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᗴ")):
            bstack1ll1l111l1l_opy_ = args[1].get_records(when)
            if not bstack1ll1l111l1l_opy_:
                continue
            records = [
                bstack1ll11l111l1_opy_(
                    kind=TestFramework.bstack1ll1l11ll1l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1ll11_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠥᗵ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1ll11_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࠤᗶ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1l111l1l_opy_
                if isinstance(getattr(r, bstack1ll11_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥᗷ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll111l111l_opy_, bstack1ll11llll1l_opy_ = bstack1l1llll1lll_opy_.get(when, (None, None))
            bstack1ll1l1ll1ll_opy_ = TestFramework.get_state(instance, bstack1ll111l111l_opy_, None) if bstack1ll111l111l_opy_ else None
            bstack1ll111ll111_opy_ = TestFramework.get_state(instance, bstack1ll11llll1l_opy_, None) if bstack1ll1l1ll1ll_opy_ else None
            if isinstance(bstack1ll111ll111_opy_, dict) and len(bstack1ll111ll111_opy_.get(bstack1ll1l1ll1ll_opy_, [])) > 0:
                hook = bstack1ll111ll111_opy_[bstack1ll1l1ll1ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l111ll_opy_ in hook:
                    hook[TestFramework.bstack1ll11l111ll_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11l1111l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11ll11l1_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l1l11lll1l_opy_.__1ll11l1ll11_opy_(test.location) if hasattr(test, bstack1ll11_opy_ (u"ࠥࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᗸ")) else getattr(test, bstack1ll11_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᗹ"), None)
        test_name = test.name if hasattr(test, bstack1ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᗺ")) else None
        bstack1ll1111llll_opy_ = test.fspath.strpath if hasattr(test, bstack1ll11_opy_ (u"ࠨࡦࡴࡲࡤࡸ࡭ࠨᗻ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll1111llll_opy_:
            return None
        code = None
        if hasattr(test, bstack1ll11_opy_ (u"ࠢࡰࡤ࡭ࠦᗼ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll1lll1_opy_ = []
        try:
            bstack11llll1lll1_opy_ = bstack1l11l1ll_opy_.bstack1l1l1ll1_opy_(test)
        except:
            bstack1l1l11lll1l_opy_.logger.warning(bstack1ll11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡷࡩࡸࡺࠠࡴࡥࡲࡴࡪࡹࠬࠡࡶࡨࡷࡹࠦࡳࡤࡱࡳࡩࡸࠦࡷࡪ࡮࡯ࠤࡧ࡫ࠠࡳࡧࡶࡳࡱࡼࡥࡥࠢ࡬ࡲࠥࡉࡌࡊࠤᗽ"))
        return {
            TestFramework.bstack1lll1l11ll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11ll111l_opy_: test_id,
            TestFramework.bstack1ll1ll11111_opy_: test_name,
            TestFramework.bstack1ll1l11l11l_opy_: getattr(test, bstack1ll11_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᗾ"), None),
            TestFramework.bstack1ll1l11l111_opy_: bstack1ll1111llll_opy_,
            TestFramework.bstack1ll1ll11l1l_opy_: bstack1l1l11lll1l_opy_.__1ll111ll1l1_opy_(test),
            TestFramework.bstack1ll111l1ll1_opy_: code,
            TestFramework.bstack1lll1llll1l_opy_: TestFramework.bstack1ll1ll111ll_opy_,
            TestFramework.bstack1lll11ll1ll_opy_: test_id,
            TestFramework.bstack1l1111l1lll_opy_: bstack11llll1lll1_opy_
        }
    @staticmethod
    def __1ll111ll1l1_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack1ll11_opy_ (u"ࠥࡳࡼࡴ࡟࡮ࡣࡵ࡯ࡪࡸࡳࠣᗿ"), [])
            markers.extend([getattr(m, bstack1ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᘀ"), None) for m in own_markers if getattr(m, bstack1ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᘁ"), None)])
            current = getattr(current, bstack1ll11_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨᘂ"), None)
        return markers
    @staticmethod
    def __1ll11l1ll11_opy_(location):
        return bstack1ll11_opy_ (u"ࠢ࠻࠼ࠥᘃ").join(filter(lambda x: isinstance(x, str), location))