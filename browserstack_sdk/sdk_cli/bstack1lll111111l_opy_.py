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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1111_opy_,
    bstack1lll1111l1l_opy_,
    bstack1llll111l1l_opy_,
    bstack1lll1llllll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll111ll_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_, bstack1lll1l1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll1l1ll11_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll11ll11l_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1ll1lllll1l_opy_(bstack1lll1l1ll11_opy_):
    bstack1lll1l1l11l_opy_ = bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡵ࡭ࡻ࡫ࡲࡴࠤᆑ")
    bstack1llll1111l1_opy_ = bstack11111_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᆒ")
    bstack1lll11lllll_opy_ = bstack11111_opy_ (u"ࠧࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᆓ")
    bstack1lll1llll11_opy_ = bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᆔ")
    bstack1lll11l1lll_opy_ = bstack11111_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡥࡲࡦࡨࡶࠦᆕ")
    bstack1lll1l111ll_opy_ = bstack11111_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡣࡳࡧࡤࡸࡪࡪࠢᆖ")
    bstack1lll11l1ll1_opy_ = bstack11111_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧᆗ")
    bstack1lll1l111l1_opy_ = bstack11111_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡵࡷࡥࡹࡻࡳࠣᆘ")
    def __init__(self):
        super().__init__(bstack1lll1ll1l11_opy_=self.bstack1lll1l1l11l_opy_, frameworks=[bstack1lllll1111l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llll11ll11_opy_((bstack1lll1ll111l_opy_.BEFORE_EACH, bstack1lll1ll1l1l_opy_.POST), self.bstack1lll111lll1_opy_)
        TestFramework.bstack1llll11ll11_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1ll1l1l_opy_.PRE), self.bstack1lll11ll1l1_opy_)
        TestFramework.bstack1llll11ll11_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1ll1l1l_opy_.POST), self.bstack1lll1ll1ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11111l1_opy_ = self.bstack1lll1111ll1_opy_(instance.context)
        if not bstack1lll11111l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᆙ") + str(bstack1llll11ll1l_opy_) + bstack11111_opy_ (u"ࠧࠨᆚ"))
        f.bstack1lllllll11l_opy_(instance, bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_, bstack1lll11111l1_opy_)
        bstack1lll111l1l1_opy_ = self.bstack1lll1111ll1_opy_(instance.context, bstack1lll111ll11_opy_=False)
        f.bstack1lllllll11l_opy_(instance, bstack1ll1lllll1l_opy_.bstack1lll11lllll_opy_, bstack1lll111l1l1_opy_)
    def bstack1lll11ll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111lll1_opy_(f, instance, bstack1llll11ll1l_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1lll11l1ll1_opy_, False):
            self.__1lll111l1ll_opy_(f,instance,bstack1llll11ll1l_opy_)
    def bstack1lll1ll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111lll1_opy_(f, instance, bstack1llll11ll1l_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1lll11l1ll1_opy_, False):
            self.__1lll111l1ll_opy_(f, instance, bstack1llll11ll1l_opy_)
        if not f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1lll1l111l1_opy_, False):
            self.__1lll111l11l_opy_(f, instance, bstack1llll11ll1l_opy_)
    def bstack1ll1llllll1_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11111ll_opy_(instance):
            return
        if f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1lll1l111l1_opy_, False):
            return
        driver.execute_script(
            bstack11111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᆛ").format(
                json.dumps(
                    {
                        bstack11111_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᆜ"): bstack11111_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᆝ"),
                        bstack11111_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᆞ"): {bstack11111_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᆟ"): result},
                    }
                )
            )
        )
        f.bstack1lllllll11l_opy_(instance, bstack1ll1lllll1l_opy_.bstack1lll1l111l1_opy_, True)
    def bstack1lll1111ll1_opy_(self, context: bstack1lll1llllll_opy_, bstack1lll111ll11_opy_= True):
        if bstack1lll111ll11_opy_:
            bstack1lll11111l1_opy_ = self.bstack1lll1lll1l1_opy_(context, reverse=True)
        else:
            bstack1lll11111l1_opy_ = self.bstack1lll11ll1ll_opy_(context, reverse=True)
        return [f for f in bstack1lll11111l1_opy_ if f[1].state != bstack1lllllll1l1_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1llll1l11l_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def __1lll111l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᆠ")).get(bstack11111_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᆡ")):
            bstack1lll11111l1_opy_ = f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_, [])
            if not bstack1lll11111l1_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᆢ") + str(bstack1llll11ll1l_opy_) + bstack11111_opy_ (u"ࠢࠣᆣ"))
                return
            driver = bstack1lll11111l1_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll11llll1_opy_, None)
            if not status:
                self.logger.debug(bstack11111_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᆤ") + str(bstack1llll11ll1l_opy_) + bstack11111_opy_ (u"ࠤࠥᆥ"))
                return
            bstack1lll1l1111l_opy_ = {bstack11111_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᆦ"): status.lower()}
            bstack1lll1l11l11_opy_ = f.get_state(instance, TestFramework.bstack1lll1l11lll_opy_, None)
            if status.lower() == bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᆧ") and bstack1lll1l11l11_opy_ is not None:
                bstack1lll1l1111l_opy_[bstack11111_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᆨ")] = bstack1lll1l11l11_opy_[0][bstack11111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᆩ")][0] if isinstance(bstack1lll1l11l11_opy_, list) else str(bstack1lll1l11l11_opy_)
            driver.execute_script(
                bstack11111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆪ").format(
                    json.dumps(
                        {
                            bstack11111_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆫ"): bstack11111_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᆬ"),
                            bstack11111_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆭ"): bstack1lll1l1111l_opy_,
                        }
                    )
                )
            )
            f.bstack1lllllll11l_opy_(instance, bstack1ll1lllll1l_opy_.bstack1lll1l111l1_opy_, True)
    @measure(event_name=EVENTS.bstack111l11ll1_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def __1lll111l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᆮ")).get(bstack11111_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᆯ")):
            test_name = f.get_state(instance, TestFramework.bstack1ll1lllll11_opy_, None)
            if not test_name:
                self.logger.debug(bstack11111_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧᆰ"))
                return
            bstack1lll11111l1_opy_ = f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_, [])
            if not bstack1lll11111l1_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᆱ") + str(bstack1llll11ll1l_opy_) + bstack11111_opy_ (u"ࠣࠤᆲ"))
                return
            for bstack1lll111l111_opy_, bstack1lll1111l11_opy_ in bstack1lll11111l1_opy_:
                if not bstack1lllll1111l_opy_.bstack1lll11111ll_opy_(bstack1lll1111l11_opy_):
                    continue
                driver = bstack1lll111l111_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆳ").format(
                        json.dumps(
                            {
                                bstack11111_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆴ"): bstack11111_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᆵ"),
                                bstack11111_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆶ"): {bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᆷ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1lllllll11l_opy_(instance, bstack1ll1lllll1l_opy_.bstack1lll11l1ll1_opy_, True)
    def bstack1llll111111_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        f: TestFramework,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111lll1_opy_(f, instance, bstack1llll11ll1l_opy_, *args, **kwargs)
        bstack1lll11111l1_opy_ = [d for d, _ in f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_, [])]
        if not bstack1lll11111l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡴࡰࠢ࡯࡭ࡳࡱࠢᆸ"))
            return
        if not bstack1lll11ll11l_opy_():
            self.logger.debug(bstack11111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᆹ"))
            return
        for bstack1ll1lllllll_opy_ in bstack1lll11111l1_opy_:
            driver = bstack1ll1lllllll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11111_opy_ (u"ࠤࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡕࡼࡲࡨࡀࠢᆺ") + str(timestamp)
            driver.execute_script(
                bstack11111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᆻ").format(
                    json.dumps(
                        {
                            bstack11111_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᆼ"): bstack11111_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢᆽ"),
                            bstack11111_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᆾ"): {
                                bstack11111_opy_ (u"ࠢࡵࡻࡳࡩࠧᆿ"): bstack11111_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧᇀ"),
                                bstack11111_opy_ (u"ࠤࡧࡥࡹࡧࠢᇁ"): data,
                                bstack11111_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤᇂ"): bstack11111_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥᇃ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1l1l1ll_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        f: TestFramework,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111lll1_opy_(f, instance, bstack1llll11ll1l_opy_, *args, **kwargs)
        keys = [
            bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_,
            bstack1ll1lllll1l_opy_.bstack1lll11lllll_opy_,
        ]
        bstack1lll11111l1_opy_ = []
        for key in keys:
            bstack1lll11111l1_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11111l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡢࡰࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡴࡰࠢ࡯࡭ࡳࡱࠢᇄ"))
            return
        if f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1lll1l111ll_opy_, False):
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡄࡄࡗࠤࡦࡲࡲࡦࡣࡧࡽࠥࡩࡲࡦࡣࡷࡩࡩࠨᇅ"))
            return
        self.bstack1llllll11l1_opy_()
        bstack11lll11111_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll1ll11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll11l11l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11lll1l_opy_)
        req.test_framework_state = bstack1llll11ll1l_opy_[0].name
        req.test_hook_state = bstack1llll11ll1l_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_)
        for bstack1lll111l111_opy_, driver in bstack1lll11111l1_opy_:
            try:
                webdriver = bstack1lll111l111_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11111_opy_ (u"ࠢࡘࡧࡥࡈࡷ࡯ࡶࡦࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥ࡯ࡳࠡࡐࡲࡲࡪࠦࠨࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࠣࡩࡽࡶࡩࡳࡧࡧ࠭ࠧᇆ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢᇇ")
                    if bstack1lllll1111l_opy_.get_state(driver, bstack1lllll1111l_opy_.bstack1lll111ll1l_opy_, False)
                    else bstack11111_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠣᇈ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll1111l_opy_.get_state(driver, bstack1lllll1111l_opy_.bstack1lll1l11ll1_opy_, bstack11111_opy_ (u"ࠥࠦᇉ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll1111l_opy_.get_state(driver, bstack1lllll1111l_opy_.bstack1lll11l1l1l_opy_, bstack11111_opy_ (u"ࠦࠧᇊ"))
                caps = None
                if hasattr(webdriver, bstack11111_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᇋ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11111_opy_ (u"ࠨࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࡤࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡥ࡫ࡵࡩࡨࡺ࡬ࡺࠢࡩࡶࡴࡳࠠࡥࡴ࡬ࡺࡪࡸ࠮ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᇌ"))
                    except Exception as e:
                        self.logger.debug(bstack11111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡫ࡪࡺࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠲ࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠤࠧᇍ") + str(e) + bstack11111_opy_ (u"ࠣࠤᇎ"))
                try:
                    bstack1lll1111111_opy_ = json.dumps(caps).encode(bstack11111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇏ")) if caps else bstack1lll1111lll_opy_ (u"ࠥࡿࢂࠨᇐ")
                    req.capabilities = bstack1lll1111111_opy_
                except Exception as e:
                    self.logger.debug(bstack11111_opy_ (u"ࠦ࡬࡫ࡴࡠࡥࡥࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡲࡩࠦࡳࡦࡴ࡬ࡥࡱ࡯ࡺࡦࠢࡦࡥࡵࡹࠠࡧࡱࡵࠤࡷ࡫ࡱࡶࡧࡶࡸ࠿ࠦࠢᇑ") + str(e) + bstack11111_opy_ (u"ࠧࠨᇒ"))
            except Exception as e:
                self.logger.error(bstack11111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡸࡪࡳ࠺ࠡࠤᇓ") + str(str(e)) + bstack11111_opy_ (u"ࠢࠣᇔ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l11l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11111l1_opy_ = f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_, [])
        if not bstack1lll11ll11l_opy_() and len(bstack1lll11111l1_opy_) == 0:
            bstack1lll11111l1_opy_ = f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll11111l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇕ") + str(kwargs) + bstack11111_opy_ (u"ࠤࠥᇖ"))
            return {}
        if len(bstack1lll11111l1_opy_) > 1:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇗ") + str(kwargs) + bstack11111_opy_ (u"ࠦࠧᇘ"))
            return {}
        bstack1lll111l111_opy_, bstack1lll1lll111_opy_ = bstack1lll11111l1_opy_[0]
        driver = bstack1lll111l111_opy_()
        if not driver:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇙ") + str(kwargs) + bstack11111_opy_ (u"ࠨࠢᇚ"))
            return {}
        capabilities = f.get_state(bstack1lll1lll111_opy_, bstack1lllll1111l_opy_.bstack1lll11lll11_opy_)
        if not capabilities:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇛ") + str(kwargs) + bstack11111_opy_ (u"ࠣࠤᇜ"))
            return {}
        return capabilities.get(bstack11111_opy_ (u"ࠤࡤࡰࡼࡧࡹࡴࡏࡤࡸࡨ࡮ࠢᇝ"), {})
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11111l1_opy_ = f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1llll1111l1_opy_, [])
        if not bstack1lll11ll11l_opy_() and len(bstack1lll11111l1_opy_) == 0:
            bstack1lll11111l1_opy_ = f.get_state(instance, bstack1ll1lllll1l_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll11111l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇞ") + str(kwargs) + bstack11111_opy_ (u"ࠦࠧᇟ"))
            return
        if len(bstack1lll11111l1_opy_) > 1:
            self.logger.debug(bstack11111_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇠ") + str(kwargs) + bstack11111_opy_ (u"ࠨࠢᇡ"))
        bstack1lll111l111_opy_, bstack1lll1lll111_opy_ = bstack1lll11111l1_opy_[0]
        driver = bstack1lll111l111_opy_()
        if not driver:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇢ") + str(kwargs) + bstack11111_opy_ (u"ࠣࠤᇣ"))
            return
        return driver