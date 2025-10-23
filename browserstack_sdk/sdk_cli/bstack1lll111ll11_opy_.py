# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
    bstack1lll111ll1l_opy_,
    bstack1lllll11l1l_opy_,
    bstack1lll1l1111l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111lll_opy_, bstack1lll1lll11l_opy_, bstack1lll1lll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import bstack1lll1l1l1ll_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1l1l_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11l11l1_opy_(bstack1lll1l1l1ll_opy_):
    bstack1lll1ll111l_opy_ = bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡶ࡮ࡼࡥࡳࡵࠥᅓ")
    bstack1lll1l1l11l_opy_ = bstack111111l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᅔ")
    bstack1lll1lll111_opy_ = bstack111111l_opy_ (u"ࠨ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᅕ")
    bstack1lll1l11l1l_opy_ = bstack111111l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᅖ")
    bstack1lll1llllll_opy_ = bstack111111l_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫࡟ࡳࡧࡩࡷࠧᅗ")
    bstack1llll11111l_opy_ = bstack111111l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡤࡴࡨࡥࡹ࡫ࡤࠣᅘ")
    bstack1lll1l1l111_opy_ = bstack111111l_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨᅙ")
    bstack1lll1l11ll1_opy_ = bstack111111l_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡶࡸࡦࡺࡵࡴࠤᅚ")
    def __init__(self):
        super().__init__(bstack1lll1lllll1_opy_=self.bstack1lll1ll111l_opy_, frameworks=[bstack1llllll11ll_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.BEFORE_EACH, bstack1lll1lll11l_opy_.POST), self.bstack1lll11l11ll_opy_)
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1lll1ll1lll_opy_)
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll11l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11l11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11l1111_opy_ = self.bstack1lll11l1l1l_opy_(instance.context)
        if not bstack1lll11l1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᅛ") + str(bstack1lllll1l1ll_opy_) + bstack111111l_opy_ (u"ࠨࠢᅜ"))
        f.bstack1llll1lll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, bstack1lll11l1111_opy_)
        bstack1lll11lll11_opy_ = self.bstack1lll11l1l1l_opy_(instance.context, bstack1lll11l1l11_opy_=False)
        f.bstack1llll1lll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1lll1lll111_opy_, bstack1lll11lll11_opy_)
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l11ll_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l111_opy_, False):
            self.__1lll11l1lll_opy_(f,instance,bstack1lllll1l1ll_opy_)
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l11ll_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l111_opy_, False):
            self.__1lll11l1lll_opy_(f, instance, bstack1lllll1l1ll_opy_)
        if not f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l11ll1_opy_, False):
            self.__1lll11ll1ll_opy_(f, instance, bstack1lllll1l1ll_opy_)
    def bstack1lll11l111l_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11lll1l_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l11ll1_opy_, False):
            return
        driver.execute_script(
            bstack111111l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᅝ").format(
                json.dumps(
                    {
                        bstack111111l_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᅞ"): bstack111111l_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᅟ"),
                        bstack111111l_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᅠ"): {bstack111111l_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᅡ"): result},
                    }
                )
            )
        )
        f.bstack1llll1lll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1lll1l11ll1_opy_, True)
    def bstack1lll11l1l1l_opy_(self, context: bstack1lll1l1111l_opy_, bstack1lll11l1l11_opy_= True):
        if bstack1lll11l1l11_opy_:
            bstack1lll11l1111_opy_ = self.bstack1llll111l11_opy_(context, reverse=True)
        else:
            bstack1lll11l1111_opy_ = self.bstack1llll111111_opy_(context, reverse=True)
        return [f for f in bstack1lll11l1111_opy_ if f[1].state != bstack1llll1lllll_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1l1ll1l11_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def __1lll11ll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᅢ")).get(bstack111111l_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᅣ")):
            bstack1lll11l1111_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, [])
            if not bstack1lll11l1111_opy_:
                self.logger.debug(bstack111111l_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᅤ") + str(bstack1lllll1l1ll_opy_) + bstack111111l_opy_ (u"ࠣࠤᅥ"))
                return
            driver = bstack1lll11l1111_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1ll1ll1_opy_, None)
            if not status:
                self.logger.debug(bstack111111l_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᅦ") + str(bstack1lllll1l1ll_opy_) + bstack111111l_opy_ (u"ࠥࠦᅧ"))
                return
            bstack1lll1l1l1l1_opy_ = {bstack111111l_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᅨ"): status.lower()}
            bstack1lll1ll11l1_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_, None)
            if status.lower() == bstack111111l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᅩ") and bstack1lll1ll11l1_opy_ is not None:
                bstack1lll1l1l1l1_opy_[bstack111111l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᅪ")] = bstack1lll1ll11l1_opy_[0][bstack111111l_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᅫ")][0] if isinstance(bstack1lll1ll11l1_opy_, list) else str(bstack1lll1ll11l1_opy_)
            driver.execute_script(
                bstack111111l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᅬ").format(
                    json.dumps(
                        {
                            bstack111111l_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᅭ"): bstack111111l_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᅮ"),
                            bstack111111l_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᅯ"): bstack1lll1l1l1l1_opy_,
                        }
                    )
                )
            )
            f.bstack1llll1lll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1lll1l11ll1_opy_, True)
    @measure(event_name=EVENTS.bstack1lll1ll1l1_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def __1lll11l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᅰ")).get(bstack111111l_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᅱ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11ll1l1_opy_, None)
            if not test_name:
                self.logger.debug(bstack111111l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨᅲ"))
                return
            bstack1lll11l1111_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, [])
            if not bstack1lll11l1111_opy_:
                self.logger.debug(bstack111111l_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᅳ") + str(bstack1lllll1l1ll_opy_) + bstack111111l_opy_ (u"ࠤࠥᅴ"))
                return
            for bstack1lll111llll_opy_, bstack1lll11l1ll1_opy_ in bstack1lll11l1111_opy_:
                if not bstack1llllll11ll_opy_.bstack1lll11lll1l_opy_(bstack1lll11l1ll1_opy_):
                    continue
                driver = bstack1lll111llll_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack111111l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᅵ").format(
                        json.dumps(
                            {
                                bstack111111l_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᅶ"): bstack111111l_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᅷ"),
                                bstack111111l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᅸ"): {bstack111111l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᅹ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll1lll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l111_opy_, True)
    def bstack1llll111ll1_opy_(
        self,
        instance: bstack1lll1lll1l1_opy_,
        f: TestFramework,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l11ll_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        bstack1lll11l1111_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, [])]
        if not bstack1lll11l1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࡹࠠࡵࡱࠣࡰ࡮ࡴ࡫ࠣᅺ"))
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᅻ"))
            return
        for bstack1lll11ll11l_opy_ in bstack1lll11l1111_opy_:
            driver = bstack1lll11ll11l_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack111111l_opy_ (u"ࠥࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡖࡽࡳࡩ࠺ࠣᅼ") + str(timestamp)
            driver.execute_script(
                bstack111111l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᅽ").format(
                    json.dumps(
                        {
                            bstack111111l_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᅾ"): bstack111111l_opy_ (u"ࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣᅿ"),
                            bstack111111l_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᆀ"): {
                                bstack111111l_opy_ (u"ࠣࡶࡼࡴࡪࠨᆁ"): bstack111111l_opy_ (u"ࠤࡄࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠨᆂ"),
                                bstack111111l_opy_ (u"ࠥࡨࡦࡺࡡࠣᆃ"): data,
                                bstack111111l_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࠥᆄ"): bstack111111l_opy_ (u"ࠧࡪࡥࡣࡷࡪࠦᆅ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1llll11_opy_(
        self,
        instance: bstack1lll1lll1l1_opy_,
        f: TestFramework,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l11ll_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        keys = [
            bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_,
            bstack1lll11l11l1_opy_.bstack1lll1lll111_opy_,
        ]
        bstack1lll11l1111_opy_ = []
        for key in keys:
            bstack1lll11l1111_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11l1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡣࡱࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࡹࠠࡵࡱࠣࡰ࡮ࡴ࡫ࠣᆆ"))
            return
        if f.get_state(instance, bstack1lll11l11l1_opy_.bstack1llll11111l_opy_, False):
            self.logger.debug(bstack111111l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡅࡅࡘࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡣࡳࡧࡤࡸࡪࡪࠢᆇ"))
            return
        self.bstack1llll1l1ll1_opy_()
        bstack1111ll111_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllll1l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1l11l1_opy_)
        req.test_framework_state = bstack1lllll1l1ll_opy_[0].name
        req.test_hook_state = bstack1lllll1l1ll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
        for bstack1lll111llll_opy_, driver in bstack1lll11l1111_opy_:
            try:
                webdriver = bstack1lll111llll_opy_()
                if webdriver is None:
                    self.logger.debug(bstack111111l_opy_ (u"࡙ࠣࡨࡦࡉࡸࡩࡷࡧࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠠࠩࡴࡨࡪࡪࡸࡥ࡯ࡥࡨࠤࡪࡾࡰࡪࡴࡨࡨ࠮ࠨᆈ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack111111l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣᆉ")
                    if bstack1llllll11ll_opy_.get_state(driver, bstack1llllll11ll_opy_.bstack1lll111l1ll_opy_, False)
                    else bstack111111l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠤᆊ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1llllll11ll_opy_.get_state(driver, bstack1llllll11ll_opy_.bstack1llll11ll11_opy_, bstack111111l_opy_ (u"ࠦࠧᆋ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1llllll11ll_opy_.get_state(driver, bstack1llllll11ll_opy_.bstack1lll1lll1ll_opy_, bstack111111l_opy_ (u"ࠧࠨᆌ"))
                caps = None
                if hasattr(webdriver, bstack111111l_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᆍ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack111111l_opy_ (u"ࠢࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࡥࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡦ࡬ࡶࡪࡩࡴ࡭ࡻࠣࡪࡷࡵ࡭ࠡࡦࡵ࡭ࡻ࡫ࡲ࠯ࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᆎ"))
                    except Exception as e:
                        self.logger.debug(bstack111111l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡧࡴࡲࡱࠥࡪࡲࡪࡸࡨࡶ࠳ࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠾ࠥࠨᆏ") + str(e) + bstack111111l_opy_ (u"ࠤࠥᆐ"))
                try:
                    bstack1lll111lll1_opy_ = json.dumps(caps).encode(bstack111111l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᆑ")) if caps else bstack1lll11ll111_opy_ (u"ࠦࢀࢃࠢᆒ")
                    req.capabilities = bstack1lll111lll1_opy_
                except Exception as e:
                    self.logger.debug(bstack111111l_opy_ (u"ࠧ࡭ࡥࡵࡡࡦࡦࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡳࡪࠠࡴࡧࡵ࡭ࡦࡲࡩࡻࡧࠣࡧࡦࡶࡳࠡࡨࡲࡶࠥࡸࡥࡲࡷࡨࡷࡹࡀࠠࠣᆓ") + str(e) + bstack111111l_opy_ (u"ࠨࠢᆔ"))
            except Exception as e:
                self.logger.error(bstack111111l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡹ࡫࡭࠻ࠢࠥᆕ") + str(str(e)) + bstack111111l_opy_ (u"ࠣࠤᆖ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l1111_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, [])
        if not bstack1lll1ll1l1l_opy_() and len(bstack1lll11l1111_opy_) == 0:
            bstack1lll11l1111_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1lll111_opy_, [])
        if not bstack1lll11l1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆗ") + str(kwargs) + bstack111111l_opy_ (u"ࠥࠦᆘ"))
            return {}
        if len(bstack1lll11l1111_opy_) > 1:
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆙ") + str(kwargs) + bstack111111l_opy_ (u"ࠧࠨᆚ"))
            return {}
        bstack1lll111llll_opy_, bstack1lll1l111l1_opy_ = bstack1lll11l1111_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack111111l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆛ") + str(kwargs) + bstack111111l_opy_ (u"ࠢࠣᆜ"))
            return {}
        capabilities = f.get_state(bstack1lll1l111l1_opy_, bstack1llllll11ll_opy_.bstack1lll1l1ll11_opy_)
        if not capabilities:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬࡯ࡶࡰࡧࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆝ") + str(kwargs) + bstack111111l_opy_ (u"ࠤࠥᆞ"))
            return {}
        return capabilities.get(bstack111111l_opy_ (u"ࠥࡥࡱࡽࡡࡺࡵࡐࡥࡹࡩࡨࠣᆟ"), {})
    def bstack1llll1111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l1111_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, [])
        if not bstack1lll1ll1l1l_opy_() and len(bstack1lll11l1111_opy_) == 0:
            bstack1lll11l1111_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1lll111_opy_, [])
        if not bstack1lll11l1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆠ") + str(kwargs) + bstack111111l_opy_ (u"ࠧࠨᆡ"))
            return
        if len(bstack1lll11l1111_opy_) > 1:
            self.logger.debug(bstack111111l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆢ") + str(kwargs) + bstack111111l_opy_ (u"ࠢࠣᆣ"))
        bstack1lll111llll_opy_, bstack1lll1l111l1_opy_ = bstack1lll11l1111_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆤ") + str(kwargs) + bstack111111l_opy_ (u"ࠤࠥᆥ"))
            return
        return driver