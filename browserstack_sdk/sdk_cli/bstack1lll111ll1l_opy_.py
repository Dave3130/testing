# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
    bstack1lll111llll_opy_,
    bstack111111l111_opy_,
    bstack1llll11l111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1lllll1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_, bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11ll1_opy_ import bstack1lll1ll1111_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l1llll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11llll1_opy_(bstack1lll1ll1111_opy_):
    bstack1lll1lll111_opy_ = bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡵ࡭ࡻ࡫ࡲࡴࠤᅠ")
    bstack1lll1l11l1l_opy_ = bstack1l_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᅡ")
    bstack1lll1l11lll_opy_ = bstack1l_opy_ (u"ࠧࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᅢ")
    bstack1llll11ll1l_opy_ = bstack1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᅣ")
    bstack1lll1ll111l_opy_ = bstack1l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡥࡲࡦࡨࡶࠦᅤ")
    bstack1llll111l1l_opy_ = bstack1l_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡣࡳࡧࡤࡸࡪࡪࠢᅥ")
    bstack1lll1lll11l_opy_ = bstack1l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧᅦ")
    bstack1llll111lll_opy_ = bstack1l_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡵࡷࡥࡹࡻࡳࠣᅧ")
    def __init__(self):
        super().__init__(bstack1lll1l1l11l_opy_=self.bstack1lll1lll111_opy_, frameworks=[bstack1lllll1ll1l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.BEFORE_EACH, bstack1lll1llll1l_opy_.POST), self.bstack1lll11l1ll1_opy_)
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.PRE), self.bstack1lll1lll1ll_opy_)
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.POST), self.bstack1lll1l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11l1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11l1l11_opy_ = self.bstack1lll11ll1l1_opy_(instance.context)
        if not bstack1lll11l1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᅨ") + str(bstack1lllll1ll11_opy_) + bstack1l_opy_ (u"ࠧࠨᅩ"))
        f.bstack1lllll11ll1_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, bstack1lll11l1l11_opy_)
        bstack1lll11ll11l_opy_ = self.bstack1lll11ll1l1_opy_(instance.context, bstack1lll11l11l1_opy_=False)
        f.bstack1lllll11ll1_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1l11lll_opy_, bstack1lll11ll11l_opy_)
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1ll1_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1lll11l_opy_, False):
            self.__1lll111lll1_opy_(f,instance,bstack1lllll1ll11_opy_)
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1ll1_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1lll11l_opy_, False):
            self.__1lll111lll1_opy_(f, instance, bstack1lllll1ll11_opy_)
        if not f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll111lll_opy_, False):
            self.__1lll11ll1ll_opy_(f, instance, bstack1lllll1ll11_opy_)
    def bstack1lll11l11ll_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11lll11_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll111lll_opy_, False):
            return
        driver.execute_script(
            bstack1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᅪ").format(
                json.dumps(
                    {
                        bstack1l_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᅫ"): bstack1l_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᅬ"),
                        bstack1l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅭ"): {bstack1l_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᅮ"): result},
                    }
                )
            )
        )
        f.bstack1lllll11ll1_opy_(instance, bstack1lll11llll1_opy_.bstack1llll111lll_opy_, True)
    def bstack1lll11ll1l1_opy_(self, context: bstack1llll11l111_opy_, bstack1lll11l11l1_opy_= True):
        if bstack1lll11l11l1_opy_:
            bstack1lll11l1l11_opy_ = self.bstack1llll11llll_opy_(context, reverse=True)
        else:
            bstack1lll11l1l11_opy_ = self.bstack1lll1ll1ll1_opy_(context, reverse=True)
        return [f for f in bstack1lll11l1l11_opy_ if f[1].state != bstack1111111l11_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1l11ll1ll_opy_, stage=STAGE.bstack11ll111111_opy_)
    def __1lll11ll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᅯ")).get(bstack1l_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᅰ")):
            bstack1lll11l1l11_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, [])
            if not bstack1lll11l1l11_opy_:
                self.logger.debug(bstack1l_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᅱ") + str(bstack1lllll1ll11_opy_) + bstack1l_opy_ (u"ࠢࠣᅲ"))
                return
            driver = bstack1lll11l1l11_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1ll1lll_opy_, None)
            if not status:
                self.logger.debug(bstack1l_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᅳ") + str(bstack1lllll1ll11_opy_) + bstack1l_opy_ (u"ࠤࠥᅴ"))
                return
            bstack1lll1l1l111_opy_ = {bstack1l_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᅵ"): status.lower()}
            bstack1lll1lllll1_opy_ = f.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_, None)
            if status.lower() == bstack1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᅶ") and bstack1lll1lllll1_opy_ is not None:
                bstack1lll1l1l111_opy_[bstack1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᅷ")] = bstack1lll1lllll1_opy_[0][bstack1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᅸ")][0] if isinstance(bstack1lll1lllll1_opy_, list) else str(bstack1lll1lllll1_opy_)
            driver.execute_script(
                bstack1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᅹ").format(
                    json.dumps(
                        {
                            bstack1l_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᅺ"): bstack1l_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᅻ"),
                            bstack1l_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᅼ"): bstack1lll1l1l111_opy_,
                        }
                    )
                )
            )
            f.bstack1lllll11ll1_opy_(instance, bstack1lll11llll1_opy_.bstack1llll111lll_opy_, True)
    @measure(event_name=EVENTS.bstack1ll11ll1l1_opy_, stage=STAGE.bstack11ll111111_opy_)
    def __1lll111lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᅽ")).get(bstack1l_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᅾ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11lll1l_opy_, None)
            if not test_name:
                self.logger.debug(bstack1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧᅿ"))
                return
            bstack1lll11l1l11_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, [])
            if not bstack1lll11l1l11_opy_:
                self.logger.debug(bstack1l_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᆀ") + str(bstack1lllll1ll11_opy_) + bstack1l_opy_ (u"ࠣࠤᆁ"))
                return
            for bstack1lll111ll11_opy_, bstack1lll11ll111_opy_ in bstack1lll11l1l11_opy_:
                if not bstack1lllll1ll1l_opy_.bstack1lll11lll11_opy_(bstack1lll11ll111_opy_):
                    continue
                driver = bstack1lll111ll11_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆂ").format(
                        json.dumps(
                            {
                                bstack1l_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆃ"): bstack1l_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᆄ"),
                                bstack1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆅ"): {bstack1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᆆ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1lllll11ll1_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1lll11l_opy_, True)
    def bstack1lll1l1ll11_opy_(
        self,
        instance: bstack1llll1l1l11_opy_,
        f: TestFramework,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1ll1_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        bstack1lll11l1l11_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, [])]
        if not bstack1lll11l1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡴࡰࠢ࡯࡭ࡳࡱࠢᆇ"))
            return
        if not bstack1lll1l1llll_opy_():
            self.logger.debug(bstack1l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᆈ"))
            return
        for bstack1lll11l1l1l_opy_ in bstack1lll11l1l11_opy_:
            driver = bstack1lll11l1l1l_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1l_opy_ (u"ࠤࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡕࡼࡲࡨࡀࠢᆉ") + str(timestamp)
            driver.execute_script(
                bstack1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᆊ").format(
                    json.dumps(
                        {
                            bstack1l_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᆋ"): bstack1l_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢᆌ"),
                            bstack1l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᆍ"): {
                                bstack1l_opy_ (u"ࠢࡵࡻࡳࡩࠧᆎ"): bstack1l_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧᆏ"),
                                bstack1l_opy_ (u"ࠤࡧࡥࡹࡧࠢᆐ"): data,
                                bstack1l_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤᆑ"): bstack1l_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥᆒ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1ll11ll_opy_(
        self,
        instance: bstack1llll1l1l11_opy_,
        f: TestFramework,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1ll1_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        keys = [
            bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_,
            bstack1lll11llll1_opy_.bstack1lll1l11lll_opy_,
        ]
        bstack1lll11l1l11_opy_ = []
        for key in keys:
            bstack1lll11l1l11_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11l1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡢࡰࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡴࡰࠢ࡯࡭ࡳࡱࠢᆓ"))
            return
        if f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll111l1l_opy_, False):
            self.logger.debug(bstack1l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡄࡄࡗࠤࡦࡲࡲࡦࡣࡧࡽࠥࡩࡲࡦࡣࡷࡩࡩࠨᆔ"))
            return
        self.bstack1lllll1l111_opy_()
        bstack1l1111lll_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1lllll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_state = bstack1lllll1ll11_opy_[0].name
        req.test_hook_state = bstack1lllll1ll11_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11ll11_opy_)
        for bstack1lll111ll11_opy_, driver in bstack1lll11l1l11_opy_:
            try:
                webdriver = bstack1lll111ll11_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1l_opy_ (u"ࠢࡘࡧࡥࡈࡷ࡯ࡶࡦࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥ࡯ࡳࠡࡐࡲࡲࡪࠦࠨࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࠣࡩࡽࡶࡩࡳࡧࡧ࠭ࠧᆕ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢᆖ")
                    if bstack1lllll1ll1l_opy_.get_state(driver, bstack1lllll1ll1l_opy_.bstack1lll11l111l_opy_, False)
                    else bstack1l_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠣᆗ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll1ll1l_opy_.get_state(driver, bstack1lllll1ll1l_opy_.bstack1llll111ll1_opy_, bstack1l_opy_ (u"ࠥࠦᆘ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll1ll1l_opy_.get_state(driver, bstack1lllll1ll1l_opy_.bstack1llll11lll1_opy_, bstack1l_opy_ (u"ࠦࠧᆙ"))
                caps = None
                if hasattr(webdriver, bstack1l_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᆚ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1l_opy_ (u"ࠨࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࡤࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡥ࡫ࡵࡩࡨࡺ࡬ࡺࠢࡩࡶࡴࡳࠠࡥࡴ࡬ࡺࡪࡸ࠮ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᆛ"))
                    except Exception as e:
                        self.logger.debug(bstack1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡫ࡪࡺࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠲ࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠤࠧᆜ") + str(e) + bstack1l_opy_ (u"ࠣࠤᆝ"))
                try:
                    bstack1lll11l1111_opy_ = json.dumps(caps).encode(bstack1l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᆞ")) if caps else bstack1lll11l1lll_opy_ (u"ࠥࡿࢂࠨᆟ")
                    req.capabilities = bstack1lll11l1111_opy_
                except Exception as e:
                    self.logger.debug(bstack1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡥࡥࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡲࡩࠦࡳࡦࡴ࡬ࡥࡱ࡯ࡺࡦࠢࡦࡥࡵࡹࠠࡧࡱࡵࠤࡷ࡫ࡱࡶࡧࡶࡸ࠿ࠦࠢᆠ") + str(e) + bstack1l_opy_ (u"ࠧࠨᆡ"))
            except Exception as e:
                self.logger.error(bstack1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡸࡪࡳ࠺ࠡࠤᆢ") + str(str(e)) + bstack1l_opy_ (u"ࠢࠣᆣ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l1l11_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll1l1llll_opy_() and len(bstack1lll11l1l11_opy_) == 0:
            bstack1lll11l1l11_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1l11lll_opy_, [])
        if not bstack1lll11l1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆤ") + str(kwargs) + bstack1l_opy_ (u"ࠤࠥᆥ"))
            return {}
        if len(bstack1lll11l1l11_opy_) > 1:
            self.logger.debug(bstack1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆦ") + str(kwargs) + bstack1l_opy_ (u"ࠦࠧᆧ"))
            return {}
        bstack1lll111ll11_opy_, bstack1llll1111ll_opy_ = bstack1lll11l1l11_opy_[0]
        driver = bstack1lll111ll11_opy_()
        if not driver:
            self.logger.debug(bstack1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆨ") + str(kwargs) + bstack1l_opy_ (u"ࠨࠢᆩ"))
            return {}
        capabilities = f.get_state(bstack1llll1111ll_opy_, bstack1lllll1ll1l_opy_.bstack1lll1llllll_opy_)
        if not capabilities:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆪ") + str(kwargs) + bstack1l_opy_ (u"ࠣࠤᆫ"))
            return {}
        return capabilities.get(bstack1l_opy_ (u"ࠤࡤࡰࡼࡧࡹࡴࡏࡤࡸࡨ࡮ࠢᆬ"), {})
    def bstack1lll1llll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l1l11_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll1l1llll_opy_() and len(bstack1lll11l1l11_opy_) == 0:
            bstack1lll11l1l11_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1l11lll_opy_, [])
        if not bstack1lll11l1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆭ") + str(kwargs) + bstack1l_opy_ (u"ࠦࠧᆮ"))
            return
        if len(bstack1lll11l1l11_opy_) > 1:
            self.logger.debug(bstack1l_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆯ") + str(kwargs) + bstack1l_opy_ (u"ࠨࠢᆰ"))
        bstack1lll111ll11_opy_, bstack1llll1111ll_opy_ = bstack1lll11l1l11_opy_[0]
        driver = bstack1lll111ll11_opy_()
        if not driver:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆱ") + str(kwargs) + bstack1l_opy_ (u"ࠣࠤᆲ"))
            return
        return driver