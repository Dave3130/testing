# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1lll1111_opy_, bstack111l111lll1_opy_
from bstack_utils.bstack11l1l11l1l_opy_ import bstack11l111l11l1_opy_
class bstack1llll11l_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111lll1l_opy_=None, bstack111111ll1ll_opy_=True, bstack1ll1l1l11ll_opy_=None, bstack11l11111l_opy_=None, result=None, duration=None, bstack1lll1l1l_opy_=None, meta={}):
        self.bstack1lll1l1l_opy_ = bstack1lll1l1l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111ll1ll_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111lll1l_opy_ = bstack111111lll1l_opy_
        self.bstack1ll1l1l11ll_opy_ = bstack1ll1l1l11ll_opy_
        self.bstack11l11111l_opy_ = bstack11l11111l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1ll111ll_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1111l_opy_(self, meta):
        self.meta = meta
    def bstack111lll1l_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111l1ll1_opy_(self):
        bstack1111111llll_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭Ἄ"): bstack1111111llll_opy_,
            bstack11ll_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭Ἅ"): bstack1111111llll_opy_,
            bstack11ll_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪἎ"): bstack1111111llll_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11ll_opy_ (u"ࠨࡕ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࠿ࠦࠢἏ") + key)
            setattr(self, key, val)
    def bstack111111ll11l_opy_(self):
        return {
            bstack11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬἐ"): self.name,
            bstack11ll_opy_ (u"ࠨࡤࡲࡨࡾ࠭ἑ"): {
                bstack11ll_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧἒ"): bstack11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪἓ"),
                bstack11ll_opy_ (u"ࠫࡨࡵࡤࡦࠩἔ"): self.code
            },
            bstack11ll_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬἕ"): self.scope,
            bstack11ll_opy_ (u"࠭ࡴࡢࡩࡶࠫ἖"): self.tags,
            bstack11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ἗"): self.framework,
            bstack11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬἘ"): self.started_at
        }
    def bstack111111l1111_opy_(self):
        return {
         bstack11ll_opy_ (u"ࠩࡰࡩࡹࡧࠧἙ"): self.meta
        }
    def bstack111111l1lll_opy_(self):
        return {
            bstack11ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭Ἒ"): {
                bstack11ll_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨἛ"): self.bstack111111lll1l_opy_
            }
        }
    def bstack111111l1l11_opy_(self, bstack111111lllll_opy_, details):
        step = next(filter(lambda st: st[bstack11ll_opy_ (u"ࠬ࡯ࡤࠨἜ")] == bstack111111lllll_opy_, self.meta[bstack11ll_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἝ")]), None)
        step.update(details)
    def bstack11l11lll_opy_(self, bstack111111lllll_opy_):
        step = next(filter(lambda st: st[bstack11ll_opy_ (u"ࠧࡪࡦࠪ἞")] == bstack111111lllll_opy_, self.meta[bstack11ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧ἟")]), None)
        step.update({
            bstack11ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ἠ"): bstack1lll1111_opy_()
        })
    def bstack1l111lll_opy_(self, bstack111111lllll_opy_, result, duration=None):
        bstack1ll1l1l11ll_opy_ = bstack1lll1111_opy_()
        if bstack111111lllll_opy_ is not None and self.meta.get(bstack11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἡ")):
            step = next(filter(lambda st: st[bstack11ll_opy_ (u"ࠫ࡮ࡪࠧἢ")] == bstack111111lllll_opy_, self.meta[bstack11ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἣ")]), None)
            step.update({
                bstack11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫἤ"): bstack1ll1l1l11ll_opy_,
                bstack11ll_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩἥ"): duration if duration else bstack111l111lll1_opy_(step[bstack11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬἦ")], bstack1ll1l1l11ll_opy_),
                bstack11ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἧ"): result.result,
                bstack11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫἨ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111l111l_opy_):
        if self.meta.get(bstack11ll_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἩ")):
            self.meta[bstack11ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἪ")].append(bstack111111l111l_opy_)
        else:
            self.meta[bstack11ll_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἫ")] = [ bstack111111l111l_opy_ ]
    def bstack111111ll111_opy_(self):
        return {
            bstack11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἬ"): self.bstack1ll111ll_opy_(),
            **self.bstack111111ll11l_opy_(),
            **self.bstack111111l1ll1_opy_(),
            **self.bstack111111l1111_opy_()
        }
    def bstack111111ll1l1_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭Ἥ"): self.bstack1ll1l1l11ll_opy_,
            bstack11ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪἮ"): self.duration,
            bstack11ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἯ"): self.result.result
        }
        if data[bstack11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫἰ")] == bstack11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬἱ"):
            data[bstack11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬἲ")] = self.result.bstack1111111ll1_opy_()
            data[bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨἳ")] = [{bstack11ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫἴ"): self.result.bstack111l11l1lll_opy_()}]
        return data
    def bstack111111l1l1l_opy_(self):
        return {
            bstack11ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧἵ"): self.bstack1ll111ll_opy_(),
            **self.bstack111111ll11l_opy_(),
            **self.bstack111111l1ll1_opy_(),
            **self.bstack111111ll1l1_opy_(),
            **self.bstack111111l1111_opy_()
        }
    def bstack1ll11lll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11ll_opy_ (u"ࠪࡗࡹࡧࡲࡵࡧࡧࠫἶ") in event:
            return self.bstack111111ll111_opy_()
        elif bstack11ll_opy_ (u"ࠫࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ἷ") in event:
            return self.bstack111111l1l1l_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l1l11ll_opy_ = time if time else bstack1lll1111_opy_()
        self.duration = duration if duration else bstack111l111lll1_opy_(self.started_at, self.bstack1ll1l1l11ll_opy_)
        if result:
            self.result = result
class bstack1l1l1l11_opy_(bstack1llll11l_opy_):
    def __init__(self, hooks=[], bstack1l1ll111_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1ll111_opy_ = bstack1l1ll111_opy_
        super().__init__(*args, **kwargs, bstack11l11111l_opy_=bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࠪἸ"))
    @classmethod
    def bstack111111l11ll_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll_opy_ (u"࠭ࡩࡥࠩἹ"): id(step),
                bstack11ll_opy_ (u"ࠧࡵࡧࡻࡸࠬἺ"): step.name,
                bstack11ll_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩἻ"): step.keyword,
            })
        return bstack1l1l1l11_opy_(
            **kwargs,
            meta={
                bstack11ll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪἼ"): {
                    bstack11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨἽ"): feature.name,
                    bstack11ll_opy_ (u"ࠫࡵࡧࡴࡩࠩἾ"): feature.filename,
                    bstack11ll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪἿ"): feature.description
                },
                bstack11ll_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨὀ"): {
                    bstack11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬὁ"): scenario.name
                },
                bstack11ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧὂ"): steps,
                bstack11ll_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫὃ"): bstack11l111l11l1_opy_(test)
            }
        )
    def bstack111111l11l1_opy_(self):
        return {
            bstack11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩὄ"): self.hooks
        }
    def bstack111111llll1_opy_(self):
        if self.bstack1l1ll111_opy_:
            return {
                bstack11ll_opy_ (u"ࠫ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠪὅ"): self.bstack1l1ll111_opy_
            }
        return {}
    def bstack111111l1l1l_opy_(self):
        return {
            **super().bstack111111l1l1l_opy_(),
            **self.bstack111111l11l1_opy_()
        }
    def bstack111111ll111_opy_(self):
        return {
            **super().bstack111111ll111_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def event_key(self):
        return bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ὆")
class bstack1l111ll1_opy_(bstack1llll11l_opy_):
    def __init__(self, hook_type, *args,bstack1l1ll111_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111l1l11_opy_ = None
        self.bstack1l1ll111_opy_ = bstack1l1ll111_opy_
        super().__init__(*args, **kwargs, bstack11l11111l_opy_=bstack11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ὇"))
    def bstack1l1l1lll_opy_(self):
        return self.hook_type
    def bstack111111lll11_opy_(self):
        return {
            bstack11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪὈ"): self.hook_type
        }
    def bstack111111l1l1l_opy_(self):
        return {
            **super().bstack111111l1l1l_opy_(),
            **self.bstack111111lll11_opy_()
        }
    def bstack111111ll111_opy_(self):
        return {
            **super().bstack111111ll111_opy_(),
            bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ࠭Ὁ"): self.bstack1l1111l1l11_opy_,
            **self.bstack111111lll11_opy_()
        }
    def event_key(self):
        return bstack11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࠫὊ")
    def bstack111lllll_opy_(self, bstack1l1111l1l11_opy_):
        self.bstack1l1111l1l11_opy_ = bstack1l1111l1l11_opy_