# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import bstack1llll11l1ll_opy_, bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1llllllllll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1lllllll11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1llll_opy_, bstack1lll1l1ll11_opy_, bstack1lll11lll1l_opy_, bstack1ll1l1111l1_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1ll1lll_opy_, bstack1ll11111111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l111llll11_opy_ = [bstack11l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᏌ"), bstack11l1l11_opy_ (u"ࠣࡲࡤࡶࡪࡴࡴࠣᏍ"), bstack11l1l11_opy_ (u"ࠤࡦࡳࡳ࡬ࡩࡨࠤᏎ"), bstack11l1l11_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࠦᏏ"), bstack11l1l11_opy_ (u"ࠦࡵࡧࡴࡩࠤᏐ")]
bstack1ll11111l1l_opy_ = bstack1ll11111111_opy_()
bstack1ll11l111l1_opy_ = bstack11l1l11_opy_ (u"࡛ࠧࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠱ࠧᏑ")
bstack1l111llllll_opy_ = {
    bstack11l1l11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡉࡵࡧࡰࠦᏒ"): bstack1l111llll11_opy_,
    bstack11l1l11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡑࡣࡦ࡯ࡦ࡭ࡥࠣᏓ"): bstack1l111llll11_opy_,
    bstack11l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡏࡲࡨࡺࡲࡥࠣᏔ"): bstack1l111llll11_opy_,
    bstack11l1l11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡆࡰࡦࡹࡳࠣᏕ"): bstack1l111llll11_opy_,
    bstack11l1l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡊࡺࡴࡣࡵ࡫ࡲࡲࠧᏖ"): bstack1l111llll11_opy_
    + [
        bstack11l1l11_opy_ (u"ࠦࡴࡸࡩࡨ࡫ࡱࡥࡱࡴࡡ࡮ࡧࠥᏗ"),
        bstack11l1l11_opy_ (u"ࠧࡱࡥࡺࡹࡲࡶࡩࡹࠢᏘ"),
        bstack11l1l11_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࡩ࡯ࡨࡲࠦᏙ"),
        bstack11l1l11_opy_ (u"ࠢ࡬ࡧࡼࡻࡴࡸࡤࡴࠤᏚ"),
        bstack11l1l11_opy_ (u"ࠣࡥࡤࡰࡱࡹࡰࡦࡥࠥᏛ"),
        bstack11l1l11_opy_ (u"ࠤࡦࡥࡱࡲ࡯ࡣ࡬ࠥᏜ"),
        bstack11l1l11_opy_ (u"ࠥࡷࡹࡧࡲࡵࠤᏝ"),
        bstack11l1l11_opy_ (u"ࠦࡸࡺ࡯ࡱࠤᏞ"),
        bstack11l1l11_opy_ (u"ࠧࡪࡵࡳࡣࡷ࡭ࡴࡴࠢᏟ"),
        bstack11l1l11_opy_ (u"ࠨࡷࡩࡧࡱࠦᏠ"),
    ],
    bstack11l1l11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣ࡬ࡲ࠳࡙ࡥࡴࡵ࡬ࡳࡳࠨᏡ"): [bstack11l1l11_opy_ (u"ࠣࡵࡷࡥࡷࡺࡰࡢࡶ࡫ࠦᏢ"), bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺࡳࡧࡣ࡬ࡰࡪࡪࠢᏣ"), bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡴࡥࡲࡰࡱ࡫ࡣࡵࡧࡧࠦᏤ"), bstack11l1l11_opy_ (u"ࠦ࡮ࡺࡥ࡮ࡵࠥᏥ")],
    bstack11l1l11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡩ࡯࡯ࡨ࡬࡫࠳ࡉ࡯࡯ࡨ࡬࡫ࠧᏦ"): [bstack11l1l11_opy_ (u"ࠨࡩ࡯ࡸࡲࡧࡦࡺࡩࡰࡰࡢࡴࡦࡸࡡ࡮ࡵࠥᏧ"), bstack11l1l11_opy_ (u"ࠢࡢࡴࡪࡷࠧᏨ")],
    bstack11l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡨ࡬ࡼࡹࡻࡲࡦࡵ࠱ࡊ࡮ࡾࡴࡶࡴࡨࡈࡪ࡬ࠢᏩ"): [bstack11l1l11_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᏪ"), bstack11l1l11_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦᏫ"), bstack11l1l11_opy_ (u"ࠦ࡫ࡻ࡮ࡤࠤᏬ"), bstack11l1l11_opy_ (u"ࠧࡶࡡࡳࡣࡰࡷࠧᏭ"), bstack11l1l11_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣᏮ"), bstack11l1l11_opy_ (u"ࠢࡪࡦࡶࠦᏯ")],
    bstack11l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡨ࡬ࡼࡹࡻࡲࡦࡵ࠱ࡗࡺࡨࡒࡦࡳࡸࡩࡸࡺࠢᏰ"): [bstack11l1l11_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢᏱ"), bstack11l1l11_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࠤᏲ"), bstack11l1l11_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡢ࡭ࡳࡪࡥࡹࠤᏳ")],
    bstack11l1l11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡸࡵ࡯ࡰࡨࡶ࠳ࡉࡡ࡭࡮ࡌࡲ࡫ࡵࠢᏴ"): [bstack11l1l11_opy_ (u"ࠨࡷࡩࡧࡱࠦᏵ"), bstack11l1l11_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࠢ᏶")],
    bstack11l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤࡶࡰ࠴ࡳࡵࡴࡸࡧࡹࡻࡲࡦࡵ࠱ࡒࡴࡪࡥࡌࡧࡼࡻࡴࡸࡤࡴࠤ᏷"): [bstack11l1l11_opy_ (u"ࠤࡱࡳࡩ࡫ࠢᏸ"), bstack11l1l11_opy_ (u"ࠥࡴࡦࡸࡥ࡯ࡶࠥᏹ")],
    bstack11l1l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡲ࡬࠰ࡶࡸࡷࡻࡣࡵࡷࡵࡩࡸ࠴ࡍࡢࡴ࡮ࠦᏺ"): [bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᏻ"), bstack11l1l11_opy_ (u"ࠨࡡࡳࡩࡶࠦᏼ"), bstack11l1l11_opy_ (u"ࠢ࡬ࡹࡤࡶ࡬ࡹࠢᏽ")],
}
_1ll1l111ll1_opy_ = set()
class bstack1l1l111l1l1_opy_(bstack1llllllllll_opy_):
    bstack1l11l11l1l1_opy_ = bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡦࡨࡨࡶࡷ࡫ࡤࠣ᏾")
    bstack1l11l111lll_opy_ = bstack11l1l11_opy_ (u"ࠤࡌࡒࡋࡕࠢ᏿")
    bstack1l111ll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠥࡉࡗࡘࡏࡓࠤ᐀")
    bstack1l11l1l111l_opy_: Callable
    bstack1l11l11l111_opy_: Callable
    def __init__(self, bstack1l1l11111l1_opy_, bstack1ll1lll1111_opy_):
        super().__init__()
        self.bstack1l11l1l1111_opy_ = bstack1ll1lll1111_opy_
        if os.getenv(bstack11l1l11_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡓ࠶࠷࡙ࠣᐁ"), bstack11l1l11_opy_ (u"ࠧ࠷ࠢᐂ")) != bstack11l1l11_opy_ (u"ࠨ࠱ࠣᐃ") or not self.is_enabled():
            self.logger.warning(bstack11l1l11_opy_ (u"ࠢࠣᐄ") + str(self.__class__.__name__) + bstack11l1l11_opy_ (u"ࠣࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧࠦᐅ"))
            return
        TestFramework.bstack1llll1ll1ll_opy_((bstack1lll1l1llll_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1lll11l1ll1_opy_)
        TestFramework.bstack1llll1ll1ll_opy_((bstack1lll1l1llll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1llll111lll_opy_)
        for event in bstack1lll1l1llll_opy_:
            for state in bstack1lll11lll1l_opy_:
                TestFramework.bstack1llll1ll1ll_opy_((event, state), self.bstack1l111ll1ll1_opy_)
        bstack1l1l11111l1_opy_.bstack1llll1ll1ll_opy_((bstack1llll1l1l1l_opy_.bstack1lllll111ll_opy_, bstack1lllllll111_opy_.POST), self.bstack1l11l11llll_opy_)
        self.bstack1l11l1l111l_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l11l11l_opy_(bstack1l1l111l1l1_opy_.bstack1l11l111lll_opy_, self.bstack1l11l1l111l_opy_)
        self.bstack1l11l11l111_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l11l11l_opy_(bstack1l1l111l1l1_opy_.bstack1l111ll1l1l_opy_, self.bstack1l11l11l111_opy_)
        self.bstack1l11l1ll1l1_opy_ = builtins.print
        builtins.print = self.bstack1l11l11111l_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l111ll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1l1llll1111_opy_() and instance:
            bstack1l11l1llll1_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1llllll11l1_opy_
            if test_framework_state == bstack1lll1l1llll_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1l1llll_opy_.LOG:
                bstack1ll1111ll_opy_ = datetime.now()
                entries = f.bstack1ll111111ll_opy_(instance, bstack1llllll11l1_opy_)
                if entries:
                    self.bstack1ll1l111l1l_opy_(instance, entries)
                    instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࠤᐆ"), datetime.now() - bstack1ll1111ll_opy_)
                    f.bstack1ll11ll1l1l_opy_(instance, bstack1llllll11l1_opy_)
                instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨᐇ"), datetime.now() - bstack1l11l1llll1_opy_)
                return # do not send this event with the bstack1l11l11lll1_opy_ bstack1l11l1ll11l_opy_
            elif (
                test_framework_state == bstack1lll1l1llll_opy_.TEST
                and test_hook_state == bstack1lll11lll1l_opy_.POST
                and not f.bstack111111111l_opy_(instance, TestFramework.bstack1ll11111ll1_opy_)
            ):
                self.logger.warning(bstack11l1l11_opy_ (u"ࠦࡩࡸ࡯ࡱࡲ࡬ࡲ࡬ࠦࡤࡶࡧࠣࡸࡴࠦ࡬ࡢࡥ࡮ࠤࡴ࡬ࠠࡳࡧࡶࡹࡱࡺࡳࠡࠤᐈ") + str(TestFramework.bstack111111111l_opy_(instance, TestFramework.bstack1ll11111ll1_opy_)) + bstack11l1l11_opy_ (u"ࠧࠨᐉ"))
                f.bstack1llllll1l11_opy_(instance, bstack1l1l111l1l1_opy_.bstack1l11l11l1l1_opy_, True)
                return # do not send this event bstack1l11l1l11ll_opy_ bstack1l11l111111_opy_
            elif (
                f.get_state(instance, bstack1l1l111l1l1_opy_.bstack1l11l11l1l1_opy_, False)
                and test_framework_state == bstack1lll1l1llll_opy_.LOG_REPORT
                and test_hook_state == bstack1lll11lll1l_opy_.POST
                and f.bstack111111111l_opy_(instance, TestFramework.bstack1ll11111ll1_opy_)
            ):
                self.logger.warning(bstack11l1l11_opy_ (u"ࠨࡩ࡯࡬ࡨࡧࡹ࡯࡮ࡨࠢࡗࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡕࡇࡖࡘ࠱ࠦࡔࡦࡵࡷࡌࡴࡵ࡫ࡔࡶࡤࡸࡪ࠴ࡐࡐࡕࡗࠤࠧᐊ") + str(TestFramework.bstack111111111l_opy_(instance, TestFramework.bstack1ll11111ll1_opy_)) + bstack11l1l11_opy_ (u"ࠢࠣᐋ"))
                self.bstack1l111ll1ll1_opy_(f, instance, (bstack1lll1l1llll_opy_.TEST, bstack1lll11lll1l_opy_.POST), *args, **kwargs)
            bstack1ll1111ll_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l111l1l_opy_ = sorted(
                filter(lambda x: x.get(bstack11l1l11_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᐌ"), None), data.pop(bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᐍ"), {}).values()),
                key=lambda x: x[bstack11l1l11_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᐎ")],
            )
            if bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_ in data:
                data.pop(bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_)
            data.update({bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᐏ"): bstack1l11l111l1l_opy_})
            instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠧࡰࡳࡰࡰ࠽ࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᐐ"), datetime.now() - bstack1ll1111ll_opy_)
            bstack1ll1111ll_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l11ll1l_opy_)
            instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠨࡪࡴࡱࡱ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᐑ"), datetime.now() - bstack1ll1111ll_opy_)
            self.bstack1l11l1ll11l_opy_(instance, bstack1llllll11l1_opy_, event_json=event_json)
            instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᐒ"), datetime.now() - bstack1l11l1llll1_opy_)
    def bstack1lll11l1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1111ll11ll_opy_ import bstack1llllll1ll1_opy_
        bstack1ll1l11llll_opy_ = bstack1llllll1ll1_opy_.bstack1ll1l11l111_opy_(EVENTS.bstack1l1ll1ll1l_opy_.value)
        self.bstack1l11l1l1111_opy_.bstack1lll1l1ll1l_opy_(instance, f, bstack1llllll11l1_opy_, *args, **kwargs)
        bstack1llllll1ll1_opy_.end(EVENTS.bstack1l1ll1ll1l_opy_.value, bstack1ll1l11llll_opy_ + bstack11l1l11_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᐓ"), bstack1ll1l11llll_opy_ + bstack11l1l11_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᐔ"), status=True, failure=None, test_name=None)
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l1l1111_opy_.bstack1lll1ll111l_opy_(instance, f, bstack1llllll11l1_opy_, *args, **kwargs)
        self.bstack1l11l111l11_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l111lll111_opy_, stage=STAGE.bstack111llllll_opy_)
    def bstack1l11l111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡗࡰ࡯ࡰࡱ࡫ࡱ࡫࡚ࠥࡥࡴࡶࡖࡩࡸࡹࡩࡰࡰࡈࡺࡪࡴࡴࠡࡩࡕࡔࡈࠦࡣࡢ࡮࡯࠾ࠥࡔ࡯ࠡࡸࡤࡰ࡮ࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡦࡤࡸࡦࠨᐕ"))
            return
        bstack1ll1111ll_opy_ = datetime.now()
        try:
            r = self.bstack1llllllll11_opy_.TestSessionEvent(req)
            instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡥࡷࡧࡱࡸࠧᐖ"), datetime.now() - bstack1ll1111ll_opy_)
            f.bstack1llllll1l11_opy_(instance, self.bstack1l11l1l1111_opy_.bstack1lll1lll11l_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11l1l11_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᐗ") + str(r) + bstack11l1l11_opy_ (u"ࠨࠢᐘ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᐙ") + str(e) + bstack11l1l11_opy_ (u"ࠣࠤᐚ"))
            traceback.print_exc()
            raise e
    def bstack1l11l11llll_opy_(
        self,
        f: bstack1lllllll11l_opy_,
        _driver: object,
        exec: Tuple[bstack1llll11l1ll_opy_, str],
        _1l11l1l1lll_opy_: Tuple[bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllllll11l_opy_.bstack1l1ll1l1l1l_opy_(method_name):
            return
        if f.bstack1l1ll1llll1_opy_(*args) == bstack1lllllll11l_opy_.bstack1l11l1l1l1l_opy_:
            bstack1l11l1llll1_opy_ = datetime.now()
            screenshot = result.get(bstack11l1l11_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣᐛ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠥ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠡ࡫ࡰࡥ࡬࡫ࠠࡣࡣࡶࡩ࠻࠺ࠠࡴࡶࡵࠦᐜ"))
                return
            bstack1ll11l11l11_opy_ = self.bstack1l11l1l11l1_opy_(instance)
            if bstack1ll11l11l11_opy_:
                entry = bstack1ll1l1111l1_opy_(TestFramework.bstack1l111lllll1_opy_, screenshot)
                self.bstack1ll1l111l1l_opy_(bstack1ll11l11l11_opy_, [entry])
                instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧࡦࡵࡧࡵࡣࡪࡾࡥࡤࡷࡷࡩࠧᐝ"), datetime.now() - bstack1l11l1llll1_opy_)
            else:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠧࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡹ࡫ࡳࡵࠢࡩࡳࡷࠦࡷࡩ࡫ࡦ࡬ࠥࡺࡨࡪࡵࠣࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠠࡸࡣࡶࠤࡹࡧ࡫ࡦࡰࠣࡦࡾࠦࡤࡳ࡫ࡹࡩࡷࡃࠠࡼࡿࠥᐞ").format(instance.ref()))
        event = {}
        bstack1ll11l11l11_opy_ = self.bstack1l11l1l11l1_opy_(instance)
        if bstack1ll11l11l11_opy_:
            self.bstack1l11l1lllll_opy_(event, bstack1ll11l11l11_opy_)
            if event.get(bstack11l1l11_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᐟ")):
                self.bstack1ll1l111l1l_opy_(bstack1ll11l11l11_opy_, event[bstack11l1l11_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᐠ")])
            else:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠ࡭ࡱࡪࡷࠥ࡬࡯ࡳࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡥࡷࡧࡱࡸࠧᐡ"))
    @measure(event_name=EVENTS.bstack1l11l1111ll_opy_, stage=STAGE.bstack111llllll_opy_)
    def bstack1ll1l111l1l_opy_(
        self,
        bstack1ll11l11l11_opy_: bstack1lll1l1ll11_opy_,
        entries: List[bstack1ll1l1111l1_opy_],
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll11l11l11_opy_, TestFramework.bstack1llll1lll11_opy_)
        req.execution_context.hash = str(bstack1ll11l11l11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l11l11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l11l11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11l11l11_opy_, TestFramework.bstack1lll1lll1l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11l11l11_opy_, TestFramework.bstack1lll11lllll_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll11l11l11_opy_, TestFramework.bstack1llll111ll1_opy_)
            log_entry.test_framework_state = bstack1ll11l11l11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l1l11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᐢ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11l1l11_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐣ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1lll1llll_opy_
                log_entry.file_path = entry.bstack1l11l1_opy_
        def bstack1ll11ll1111_opy_():
            bstack1ll1111ll_opy_ = datetime.now()
            try:
                self.bstack1llllllll11_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l111lllll1_opy_:
                    bstack1ll11l11l11_opy_.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᐤ"), datetime.now() - bstack1ll1111ll_opy_)
                elif entry.kind == TestFramework.bstack1l11l1l1l11_opy_:
                    bstack1ll11l11l11_opy_.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠤᐥ"), datetime.now() - bstack1ll1111ll_opy_)
                else:
                    bstack1ll11l11l11_opy_.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥ࡬ࡰࡩࠥᐦ"), datetime.now() - bstack1ll1111ll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1l11_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᐧ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l11ll_opy_.enqueue(bstack1ll11ll1111_opy_)
    @measure(event_name=EVENTS.bstack1l111lll11l_opy_, stage=STAGE.bstack111llllll_opy_)
    def bstack1l11l1ll11l_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        event_json=None,
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1lll11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11lllll_opy_)
        req.test_framework_state = bstack1llllll11l1_opy_[0].name
        req.test_hook_state = bstack1llllll11l1_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll11lll11l_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll1l11l1ll_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l11ll1l_opy_)).encode(bstack11l1l11_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᐨ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll11ll1111_opy_():
            bstack1ll1111ll_opy_ = datetime.now()
            try:
                self.bstack1llllllll11_opy_.TestFrameworkEvent(req)
                instance.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡥࡷࡧࡱࡸࠧᐩ"), datetime.now() - bstack1ll1111ll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1l11_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᐪ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l11ll_opy_.enqueue(bstack1ll11ll1111_opy_)
    def bstack1l11l1l11l1_opy_(self, instance: bstack1llll11l1ll_opy_):
        bstack1l11l1lll11_opy_ = TestFramework.bstack1l11l111ll1_opy_(instance.context)
        for t in bstack1l11l1lll11_opy_:
            bstack1lll111l11l_opy_ = TestFramework.get_state(t, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, [])
            if any(instance is d[1] for d in bstack1lll111l11l_opy_):
                return t
    def bstack1l11l1ll1ll_opy_(self, message):
        self.bstack1l11l1l111l_opy_(message + bstack11l1l11_opy_ (u"ࠦࡡࡴࠢᐫ"))
    def log_error(self, message):
        self.bstack1l11l11l111_opy_(message + bstack11l1l11_opy_ (u"ࠧࡢ࡮ࠣᐬ"))
    def bstack1l11l11l11l_opy_(self, level, original_func):
        def bstack1l11l1111l1_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack11l1l11_opy_ (u"ࠨࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫ࠢᐭ") in message or bstack11l1l11_opy_ (u"ࠢ࡜ࡕࡇࡏࡈࡒࡉ࡞ࠤᐮ") in message or bstack11l1l11_opy_ (u"ࠣ࡝࡚ࡩࡧࡊࡲࡪࡸࡨࡶࡒࡵࡤࡶ࡮ࡨࡡࠧᐯ") in message:
                return return_value
            bstack1l11l1lll11_opy_ = TestFramework.bstack1l111ll1l11_opy_()
            if not bstack1l11l1lll11_opy_:
                return return_value
            bstack1ll11l11l11_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l1lll11_opy_
                    if TestFramework.bstack111111111l_opy_(instance, TestFramework.bstack1llll111ll1_opy_)
                ),
                None,
            )
            if not bstack1ll11l11l11_opy_:
                return return_value
            entry = bstack1ll1l1111l1_opy_(TestFramework.bstack1l1lllll1ll_opy_, message, level)
            self.bstack1ll1l111l1l_opy_(bstack1ll11l11l11_opy_, [entry])
            return return_value
        return bstack1l11l1111l1_opy_
    def bstack1l11l11111l_opy_(self):
        def bstack1l111lll1l1_opy_(*args, **kwargs):
            try:
                self.bstack1l11l1ll1l1_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack11l1l11_opy_ (u"ࠩࠣࠫᐰ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack11l1l11_opy_ (u"ࠥࡉࡻ࡫࡮ࡵࡆ࡬ࡷࡵࡧࡴࡤࡪࡨࡶࡒࡵࡤࡶ࡮ࡨࠦᐱ") in message:
                    return
                bstack1l11l1lll11_opy_ = TestFramework.bstack1l111ll1l11_opy_()
                if not bstack1l11l1lll11_opy_:
                    return
                bstack1ll11l11l11_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l1lll11_opy_
                        if TestFramework.bstack111111111l_opy_(instance, TestFramework.bstack1llll111ll1_opy_)
                    ),
                    None,
                )
                if not bstack1ll11l11l11_opy_:
                    return
                entry = bstack1ll1l1111l1_opy_(TestFramework.bstack1l1lllll1ll_opy_, message, bstack1l1l111l1l1_opy_.bstack1l11l111lll_opy_)
                self.bstack1ll1l111l1l_opy_(bstack1ll11l11l11_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l1ll1l1_opy_(bstack1lll11ll111_opy_ (u"ࠦࡠࡋࡶࡦࡰࡷࡈ࡮ࡹࡰࡢࡶࡦ࡬ࡪࡸࡍࡰࡦࡸࡰࡪࡣࠠࡍࡱࡪࠤࡨࡧࡰࡵࡷࡵࡩࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡥࡾࠤᐲ"))
                except:
                    pass
        return bstack1l111lll1l1_opy_
    def bstack1l11l1lllll_opy_(self, event: dict, instance=None) -> None:
        global _1ll1l111ll1_opy_
        levels = [bstack11l1l11_opy_ (u"࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣᐳ"), bstack11l1l11_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᐴ")]
        bstack1l111ll1lll_opy_ = bstack11l1l11_opy_ (u"ࠢࠣᐵ")
        if instance is not None:
            try:
                bstack1l111ll1lll_opy_ = TestFramework.get_state(instance, TestFramework.bstack1llll111ll1_opy_)
            except Exception as e:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡷࡸ࡭ࡩࠦࡦࡳࡱࡰࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠨᐶ").format(e))
        bstack1l111lll1ll_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᐷ")]
                bstack1ll1111lll1_opy_ = os.path.join(bstack1ll11111l1l_opy_, (bstack1ll11l111l1_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1111lll1_opy_):
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡮ࡰࡶࠣࡴࡷ࡫ࡳࡦࡰࡷࠤ࡫ࡵࡲࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡚ࠥࡥࡴࡶࠣࡥࡳࡪࠠࡃࡷ࡬ࡰࡩࠦ࡬ࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᐸ").format(bstack1ll1111lll1_opy_))
                    continue
                file_names = os.listdir(bstack1ll1111lll1_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1111lll1_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll1l111ll1_opy_:
                        self.logger.info(bstack11l1l11_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᐹ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l11ll11_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l11ll11_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack11l1l11_opy_ (u"࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣᐺ"):
                                entry = bstack1ll1l1111l1_opy_(
                                    kind=bstack11l1l11_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᐻ"),
                                    message=bstack11l1l11_opy_ (u"ࠢࠣᐼ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1lll1llll_opy_=file_size,
                                    bstack1l1lll1lll1_opy_=bstack11l1l11_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᐽ"),
                                    bstack1l11l1_opy_=os.path.abspath(file_path),
                                    bstack1l1111l1ll_opy_=bstack1l111ll1lll_opy_
                                )
                            elif level == bstack11l1l11_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᐾ"):
                                entry = bstack1ll1l1111l1_opy_(
                                    kind=bstack11l1l11_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐿ"),
                                    message=bstack11l1l11_opy_ (u"ࠦࠧᑀ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1lll1llll_opy_=file_size,
                                    bstack1l1lll1lll1_opy_=bstack11l1l11_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧᑁ"),
                                    bstack1l11l1_opy_=os.path.abspath(file_path),
                                    bstack1ll111lll1l_opy_=bstack1l111ll1lll_opy_
                                )
                            bstack1l111lll1ll_opy_.append(entry)
                            _1ll1l111ll1_opy_.add(abs_path)
                        except Exception as bstack1l11l1ll111_opy_:
                            self.logger.error(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡵࡥ࡮ࡹࡥࡥࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡾࢁࠧᑂ").format(bstack1l11l1ll111_opy_))
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡶࡦ࡯ࡳࡦࡦࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᑃ").format(e))
        event[bstack11l1l11_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᑄ")] = bstack1l111lll1ll_opy_
class bstack1l11l11ll1l_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l1lll1l_opy_ = set()
        kwargs[bstack11l1l11_opy_ (u"ࠤࡶ࡯࡮ࡶ࡫ࡦࡻࡶࠦᑅ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l11l1ll_opy_(obj, self.bstack1l11l1lll1l_opy_)
def bstack1l11ll11111_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l11l1ll_opy_(obj, bstack1l11l1lll1l_opy_=None, max_depth=3):
    if bstack1l11l1lll1l_opy_ is None:
        bstack1l11l1lll1l_opy_ = set()
    if id(obj) in bstack1l11l1lll1l_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l1lll1l_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l111llll1l_opy_ = TestFramework.bstack1ll1111l1ll_opy_(obj)
    bstack1l11l1l1ll1_opy_ = next((k.lower() in bstack1l111llll1l_opy_.lower() for k in bstack1l111llllll_opy_.keys()), None)
    if bstack1l11l1l1ll1_opy_:
        obj = TestFramework.bstack1ll1l11lll1_opy_(obj, bstack1l111llllll_opy_[bstack1l11l1l1ll1_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11l1l11_opy_ (u"ࠥࡣࡤࡹ࡬ࡰࡶࡶࡣࡤࠨᑆ")):
            keys = getattr(obj, bstack11l1l11_opy_ (u"ࠦࡤࡥࡳ࡭ࡱࡷࡷࡤࡥࠢᑇ"), [])
        elif hasattr(obj, bstack11l1l11_opy_ (u"ࠧࡥ࡟ࡥ࡫ࡦࡸࡤࡥࠢᑈ")):
            keys = getattr(obj, bstack11l1l11_opy_ (u"ࠨ࡟ࡠࡦ࡬ࡧࡹࡥ࡟ࠣᑉ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11l1l11_opy_ (u"ࠢࡠࠤᑊ"))}
        if not obj and bstack1l111llll1l_opy_ == bstack11l1l11_opy_ (u"ࠣࡲࡤࡸ࡭ࡲࡩࡣ࠰ࡓࡳࡸ࡯ࡸࡑࡣࡷ࡬ࠧᑋ"):
            obj = {bstack11l1l11_opy_ (u"ࠤࡳࡥࡹ࡮ࠢᑌ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11ll11111_opy_(key) or str(key).startswith(bstack11l1l11_opy_ (u"ࠥࡣࠧᑍ")):
            continue
        if value is not None and bstack1l11ll11111_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l11l1ll_opy_(value, bstack1l11l1lll1l_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l11l1ll_opy_(o, bstack1l11l1lll1l_opy_, max_depth) for o in value]))
    return result or None